"""Cross-model judge-consistency audit (judge v2 tooling).

Fairness check the per-task way: two models that printed ESSENTIALLY THE SAME
output for the same task must get the same verdict. For each tid we build a
feature signature from the stdout the judge actually saw (judge_inputs), then
flag pairs with matching flags + high numeric overlap but verdicts 2 vs 0.

signature:
  flags   : has_nan, has_traceback, near_empty
  numbers : values rounded to 3 significant digits (set; Jaccard overlap)

conflict := same tid, same flags, Jaccard >= 0.8, |verdict difference| == 2

Usage:
  python judge_consistency_audit.py judge_out        # v1 baseline
  python judge_consistency_audit.py judge_out_v2     # after re-judge
Writes results_v3/judge_consistency_<tag>.json + .html
"""
import glob
import json
import math
import os
import re
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")

NUM_RE = re.compile(r"-?\d+\.?\d*(?:[eE][-+]?\d+)?")
NAN_RE = re.compile(r"\bnan\b", re.I)


def sig3(x):
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + 2)


def signature(stdout):
    nums = set()
    for tok in NUM_RE.findall(stdout or ""):
        try:
            nums.add(sig3(float(tok)))
        except (ValueError, OverflowError):
            pass
    flags = (bool(NAN_RE.search(stdout or "")),
             "traceback" in (stdout or "").lower(),
             len((stdout or "").strip()) < 5)
    return flags, nums


def jaccard(a, b):
    if not a and not b:
        return 1.0
    u = a | b
    return len(a & b) / len(u) if u else 1.0


def main():
    judge_dir = sys.argv[1] if len(sys.argv) > 1 else "judge_out"
    tag = "v2" if judge_dir.endswith("v2") else "v1"
    inputs_dir = "judge_inputs_v2" if tag == "v2" else "judge_inputs"

    # records[tid] -> list of {key, verdict, reason, flags, nums, stdout}
    records = defaultdict(list)
    n_files = 0
    for f in sorted(glob.glob(os.path.join(RES, judge_dir, "*.json"))):
        name = os.path.basename(f)[:-5]
        if name.startswith("fix__"):
            continue  # never read aux files as canonical (HANDOVER trap)
        jo = json.load(open(f))
        ji_path = os.path.join(RES, inputs_dir, f"{name}.json")
        stdouts = {}
        if os.path.exists(ji_path):
            stdouts = {t["tid"]: t.get("stdout", "") for t in json.load(open(ji_path))["tasks"]}
        n_files += 1
        for v in jo["verdicts"]:
            so = stdouts.get(v["tid"], "")
            flags, nums = signature(so)
            records[v["tid"]].append({
                "key": name, "verdict": v.get("verdict"),
                "reason": v.get("reason", ""), "flags": flags, "nums": nums,
                "stdout": so[:400],
            })

    conflicts = []
    for tid, recs in records.items():
        for i in range(len(recs)):
            for j in range(i + 1, len(recs)):
                a, b = recs[i], recs[j]
                if a["verdict"] is None or b["verdict"] is None:
                    continue
                if abs(a["verdict"] - b["verdict"]) < 2:
                    continue
                if a["flags"] != b["flags"]:
                    continue
                jac = jaccard(a["nums"], b["nums"])
                if jac >= 0.8:
                    conflicts.append({
                        "tid": tid, "jaccard": round(jac, 3),
                        "flags": {"nan": a["flags"][0], "traceback": a["flags"][1],
                                  "near_empty": a["flags"][2]},
                        "a": {k: a[k] for k in ("key", "verdict", "reason", "stdout")},
                        "b": {k: b[k] for k in ("key", "verdict", "reason", "stdout")},
                    })

    conflicts.sort(key=lambda c: (c["tid"], -c["jaccard"]))
    by_tid = defaultdict(int)
    for c in conflicts:
        by_tid[c["tid"]] += 1

    out_json = os.path.join(RES, f"judge_consistency_{tag}.json")
    json.dump({"judge_dir": judge_dir, "n_files": n_files,
               "n_conflict_pairs": len(conflicts), "by_tid": dict(by_tid),
               "conflicts": conflicts}, open(out_json, "w"),
              ensure_ascii=False, indent=1)

    # ---- compact html ----
    rows = []
    for c in conflicts:
        rows.append(f"""<tr><td><b>{c['tid']}</b><br><span class=j>J={c['jaccard']}</span>
<br><span class=f>{'nan ' if c['flags']['nan'] else ''}{'tb ' if c['flags']['traceback'] else ''}</span></td>
<td class=v{c['a']['verdict']}><b>{c['a']['key']}</b> = {c['a']['verdict']}<br><i>{c['a']['reason']}</i>
<pre>{(c['a']['stdout'] or '').replace('<','&lt;')}</pre></td>
<td class=v{c['b']['verdict']}><b>{c['b']['key']}</b> = {c['b']['verdict']}<br><i>{c['b']['reason']}</i>
<pre>{(c['b']['stdout'] or '').replace('<','&lt;')}</pre></td></tr>""")
    html = f"""<!doctype html><meta charset=utf-8><title>judge consistency {tag}</title>
<style>body{{font:13px system-ui;margin:24px;max-width:1300px}}
table{{border-collapse:collapse;width:100%}}td{{border:1px solid #e5e7eb;padding:8px;vertical-align:top}}
pre{{font-size:10px;background:#f8fafc;padding:6px;border-radius:6px;white-space:pre-wrap;max-height:120px;overflow:auto}}
.v2{{background:#f0fdf4}}.v0{{background:#fef2f2}}.v1{{background:#fffbeb}}.j{{color:#6b7280;font-size:11px}}
.f{{color:#b91c1c;font-size:11px;font-weight:700}}</style>
<h2>Judge consistency audit — {judge_dir} ({len(conflicts)} conflicting pairs, {n_files} files)</h2>
<p>Pairs with the same task, same nan/traceback flags, numeric overlap &ge; 0.8, but verdicts 2 vs 0.</p>
<p>by task: {json.dumps(dict(sorted(by_tid.items(), key=lambda x: -x[1])))}</p>
<table>{''.join(rows)}</table>"""
    out_html = os.path.join(RES, f"judge_consistency_{tag}.html")
    open(out_html, "w").write(html)

    print(f"{judge_dir}: {n_files} files, {len(conflicts)} conflicting pairs")
    for tid, n in sorted(by_tid.items(), key=lambda x: -x[1])[:12]:
        print(f"  {tid}: {n}")
    print(f"wrote {out_json}\nwrote {out_html}")


if __name__ == "__main__":
    main()
