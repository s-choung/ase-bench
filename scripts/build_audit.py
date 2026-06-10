"""Build a JUDGE-THE-JUDGE audit artifact.

Joins, per (model_cond, task), every signal we have so a human can review whether
the Opus judge was right:
  - prompt, code, stdout                      (the evidence)
  - opus  verdict (2/1/0) + reason            (primary judge)
  - det   verdict (2 correct / 0 wrong / -1)  (deterministic structural anchor)
  - mini  correct True/False                  (gpt-4.1-mini spot-check, open models, n=130)

Flags DISAGREEMENTS as the cases worth human review:
  - hard conflict: det in {0,2} and opus disagrees in direction
       det=0 (structurally WRONG) but opus=2 (says correct)  -> opus may have MISSED a real error
       det=2 (structurally OK)    but opus=0 (says wrong)     -> opus may be TOO HARSH
  - mini conflict: mini and opus disagree on pass/fail

Outputs:
  results_v3/correctness_audit.json   (full join)
  results_v3/correctness_audit.html   (sortable; disagreements first)
"""
import json
import os
import re
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
V8 = os.path.join(BASE, "benchmark_report_v8.html")
JUDGE_DIR = os.path.join(RES, "judge_out")
DET = os.path.join(RES, "correctness.json")
SPOT = os.path.join(RES, "spotcheck_correctness.json")
OUT_JSON = os.path.join(RES, "correctness_audit.json")
OUT_HTML = os.path.join(RES, "correctness_audit.html")


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    h = open(V8).read()
    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))

    # opus verdicts
    opus = {}
    for f in glob.glob(os.path.join(JUDGE_DIR, "*.json")):
        d = json.load(open(f))
        key = d.get("model_cond") or os.path.basename(f)[:-5]
        opus[key] = {v["tid"]: v for v in d.get("verdicts", []) if "tid" in v}

    det = json.load(open(DET)) if os.path.exists(DET) else {}

    # gpt-4.1-mini spot-check sample (open models only), key by (alias_cond, tid)
    mini = {}
    if os.path.exists(SPOT):
        for s in json.load(open(SPOT)):
            j = s.get("judge")
            if j is None:
                continue
            mini[(f"{s['alias']}_{s['cond']}", s["tid"])] = j.get("correct")

    rows = []
    for tid, t in DATA.items():
        prompt = t.get("prompt_en") or t.get("prompt", "")
        for key, m in t["models"].items():
            if not m.get("success"):
                continue
            ov = opus.get(key, {}).get(tid)
            opus_v = ov["verdict"] if ov else None
            opus_r = ov.get("reason", "") if ov else ""
            dv = det.get(key, {}).get(tid, {})
            det_v = dv.get("verdict", None)
            det_why = dv.get("why", "")
            mv = mini.get((key, tid))  # True/False/None

            # disagreement flags
            hard = ""
            if det_v == 0 and opus_v == 2:
                hard = "det=WRONG but opus=correct (opus may have MISSED error)"
            elif det_v == 2 and opus_v == 0:
                hard = "det=ok but opus=WRONG (opus may be too harsh)"
            mini_conf = ""
            if mv is True and opus_v == 0:
                mini_conf = "mini=correct vs opus=wrong"
            elif mv is False and opus_v == 2:
                mini_conf = "mini=wrong vs opus=correct"

            rows.append({
                "model_cond": key, "tid": tid, "category": t.get("category", ""),
                "difficulty": t.get("difficulty", ""), "prompt": prompt,
                "opus": opus_v, "opus_reason": opus_r,
                "det": det_v, "det_why": det_why,
                "mini": mv, "hard_conflict": hard, "mini_conflict": mini_conf,
                "code": m.get("code", ""), "stdout": m.get("stdout", ""),
            })

    json.dump(rows, open(OUT_JSON, "w"), ensure_ascii=False, indent=1)

    # ---- agreement stats ----
    det_checkable = [r for r in rows if r["det"] in (0, 2)]
    agree = sum(1 for r in det_checkable
                if (r["det"] == 2 and r["opus"] in (1, 2)) or (r["det"] == 0 and r["opus"] == 0))
    hard = [r for r in rows if r["hard_conflict"]]
    miss = [r for r in rows if r["det"] == 0 and r["opus"] == 2]   # opus missed a structural error
    harsh = [r for r in rows if r["det"] == 2 and r["opus"] == 0]
    mini_checkable = [r for r in rows if r["mini"] is not None]
    mini_agree = sum(1 for r in mini_checkable
                     if (r["mini"] and r["opus"] in (1, 2)) or (not r["mini"] and r["opus"] == 0))

    print(f"total judged PASS rows: {len(rows)}")
    print(f"Opus vs deterministic (checkable n={len(det_checkable)}): "
          f"agree {agree} ({100*agree/max(len(det_checkable),1):.0f}%)")
    print(f"  hard conflicts: {len(hard)}  | opus MISSED structural error: {len(miss)} | "
          f"opus too harsh: {len(harsh)}")
    print(f"Opus vs gpt-4.1-mini (checkable n={len(mini_checkable)}): "
          f"agree {mini_agree} ({100*mini_agree/max(len(mini_checkable),1):.0f}%)")

    # ---- HTML: disagreements first ----
    def vbadge(v, kind):
        if kind == "opus":
            lab = {2: "correct", 1: "partial", 0: "WRONG", None: "—"}.get(v, "—")
            bg = {2: "#16a34a", 1: "#f59e0b", 0: "#dc2626", None: "#9ca3af"}.get(v, "#9ca3af")
        elif kind == "det":
            lab = {2: "ok", 0: "WRONG", -1: "n/a", None: "—"}.get(v, "—")
            bg = {2: "#16a34a", 0: "#dc2626", -1: "#9ca3af", None: "#9ca3af"}.get(v, "#9ca3af")
        else:
            lab = {True: "correct", False: "WRONG", None: "—"}.get(v, "—")
            bg = {True: "#16a34a", False: "#dc2626", None: "#9ca3af"}.get(v, "#9ca3af")
        c = "#000" if (kind == "opus" and v == 1) else "#fff"
        return f'<span style="background:{bg};color:{c};padding:1px 7px;border-radius:4px;font-size:11px;font-weight:700">{lab}</span>'

    rows_sorted = sorted(rows, key=lambda r: (0 if r["hard_conflict"] else 1 if r["mini_conflict"] else 2,
                                              r["model_cond"], r["tid"]))
    cards = []
    for r in rows_sorted:
        flag = ""
        if r["hard_conflict"]:
            flag = f'<div style="background:#fef2f2;border-left:3px solid #dc2626;padding:4px 8px;margin:4px 0;font-size:12px;color:#991b1b">⚠ {esc(r["hard_conflict"])}</div>'
        elif r["mini_conflict"]:
            flag = f'<div style="background:#fffbeb;border-left:3px solid #f59e0b;padding:4px 8px;margin:4px 0;font-size:12px;color:#92400e">⚠ {esc(r["mini_conflict"])}</div>'
        cards.append(f'''<div class="row" data-conflict="{1 if r["hard_conflict"] else 2 if r["mini_conflict"] else 0}">
  <div class="rhead"><b>{r["model_cond"]}</b> · {r["tid"]} <span class="cat">{r["category"]}/{r["difficulty"]}</span>
    &nbsp; opus {vbadge(r["opus"],"opus")} det {vbadge(r["det"],"det")} mini {vbadge(r["mini"],"mini")}</div>
  {flag}
  <div class="prompt">{esc(r["prompt"])}</div>
  <div class="reason"><b>opus:</b> {esc(r["opus_reason"])} &nbsp; <span class="det"><b>det:</b> {esc(r["det_why"])}</span></div>
  <details><summary>code + stdout</summary>
    <pre class="code">{esc(r["code"][:4000])}</pre>
    <div class="lbl">stdout:</div><pre class="out">{esc(r["stdout"][:1500])}</pre>
  </details>
</div>''')

    html = f'''<!doctype html><meta charset="utf-8"><title>ASE correctness — judge the judge</title>
<style>
body{{font:14px/1.5 -apple-system,system-ui,sans-serif;max-width:1100px;margin:0 auto;padding:20px;color:#1f2937;background:#f9fafb}}
h1{{font-size:20px}} .stats{{background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:12px 16px;margin:12px 0;font-size:13px}}
.controls{{position:sticky;top:0;background:#f9fafb;padding:8px 0;border-bottom:1px solid #e5e7eb;z-index:5}}
.row{{background:#fff;border:1px solid #e5e7eb;border-radius:8px;padding:10px 14px;margin:8px 0}}
.rhead{{font-size:13px}} .cat{{color:#6b7280;font-size:11px}}
.prompt{{color:#374151;font-size:13px;margin:4px 0}}
.reason{{font-size:12px;color:#4b5563;background:#f3f4f6;border-radius:5px;padding:5px 8px}}
.reason .det{{color:#6b7280}}
details{{margin-top:6px}} summary{{cursor:pointer;font-size:12px;color:#2563eb}}
pre{{background:#0b1021;color:#d6deeb;padding:10px;border-radius:6px;overflow:auto;font-size:11px;max-height:340px}}
pre.out{{background:#111827;max-height:200px}} .lbl{{font-size:11px;color:#6b7280;margin-top:4px}}
button{{font:13px sans-serif;padding:5px 12px;margin-right:6px;border:1px solid #d1d5db;border-radius:6px;background:#fff;cursor:pointer}}
button.active{{background:#1f2937;color:#fff;border-color:#1f2937}}
</style>
<h1>ASE-bench correctness — judge the judge</h1>
<div class="stats">
<b>Opus vs deterministic anchor</b> (structural tasks, n={len(det_checkable)}): agree {100*agree/max(len(det_checkable),1):.0f}% &nbsp;|&nbsp;
hard conflicts: <b>{len(hard)}</b> (opus missed structural error: {len(miss)} · opus too harsh: {len(harsh)})<br>
<b>Opus vs gpt-4.1-mini sample</b> (n={len(mini_checkable)}): agree {100*mini_agree/max(len(mini_checkable),1):.0f}%<br>
<span style="color:#6b7280">det = deterministic expected-output (objective where computable; n/a otherwise). mini = gpt-4.1-mini spot-check (open models only). Disagreements are shown first — review these to validate the Opus judge.</span>
</div>
<div class="controls">
<button class="active" onclick="filt(0,this)">All ({len(rows)})</button>
<button onclick="filt(1,this)">Hard conflicts ({len(hard)})</button>
<button onclick="filt(2,this)">Any disagreement ({len(hard)+sum(1 for r in rows if r["mini_conflict"] and not r["hard_conflict"])})</button>
</div>
{''.join(cards)}
<script>
function filt(mode,btn){{
  document.querySelectorAll('.controls button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');
  document.querySelectorAll('.row').forEach(r=>{{
    const c=+r.dataset.conflict;
    r.style.display = (mode===0)||(mode===1&&c===1)||(mode===2&&c>0) ? '' : 'none';
  }});
}}
</script>'''
    open(OUT_HTML, "w").write(html)
    print(f"wrote {OUT_JSON}\nwrote {OUT_HTML}")


if __name__ == "__main__":
    main()
