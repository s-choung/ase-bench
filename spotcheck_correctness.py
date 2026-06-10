"""Spot-check ASE-bench CORRECTNESS — the harness scores success=returncode==0
("does it RUN"), which lets false positives through (code runs but solves the task
WRONG, e.g. solar T01 PASS with `Cu*2*2*2` giving the wrong supercell).

This tool samples PASS cases and judges whether they're actually CORRECT, so we can
estimate the false-positive rate before deciding whether to build a full
expected-output checker.

Two modes:
  (default)  EXTRACT — pull (prompt, code, stdout) for a seeded random sample of
             PASS cases per model_cond into a markdown file for human/LLM review.
  --judge    LLM-JUDGE — additionally ask a cheap model "did this code correctly
             accomplish the task?" (yes/no/unsure) and tabulate false-positive rate.

Reads: results_v3/openrouter/<alias>.json (success, exec.stdout) +
       generated_v3/eng/<alias>_<cond>/task_NN.py (code).
No re-execution. Usage:
  python spotcheck_correctness.py [--n 5] [--judge] [--judge-model gpt-4.1-mini]
"""
import argparse
import glob
import json
import os
import random
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.join(BASE, "results_v3", "openrouter")
GEN_DIR = os.path.join(BASE, "generated_v3", "eng")
PROMPTS_FILE = os.path.join(BASE, "prompts_50_eng.json")
OUT_MD = os.path.join(BASE, "results_v3", "spotcheck_correctness.md")
OUT_JSON = os.path.join(BASE, "results_v3", "spotcheck_correctness.json")

SEED = 20260608  # fixed so the sample is reproducible


def load_prompts():
    return {t["id"]: t for t in json.load(open(PROMPTS_FILE))["tasks"]}


def read_code(alias, cond, tid):
    num = tid[1:].zfill(2)
    fp = os.path.join(GEN_DIR, f"{alias}_{cond}", f"task_{num}.py")
    return open(fp).read() if os.path.exists(fp) else ""


def collect(n):
    """For each model_cond, seeded-random n PASS cases -> sample records."""
    prompts = load_prompts()
    samples = []
    for f in sorted(glob.glob(os.path.join(RES_DIR, "*.json"))):
        alias = os.path.basename(f)[:-5]
        r = json.load(open(f))
        for cond in ("vanilla", "skill_v3"):
            key = f"{alias}_{cond}"
            d = r.get(key, {})
            passes = [tid for tid, v in d.items() if v.get("success")]
            if not passes:
                continue
            rng = random.Random(f"{SEED}-{key}")
            pick = rng.sample(passes, min(n, len(passes)))
            for tid in pick:
                v = d[tid]
                samples.append({
                    "alias": alias, "cond": cond, "tid": tid,
                    "category": v.get("category", ""),
                    "difficulty": v.get("difficulty", ""),
                    "prompt": prompts.get(tid, {}).get("prompt", v.get("prompt", "")),
                    "tests_api": prompts.get(tid, {}).get("tests_api", ""),
                    "code": read_code(alias, cond, tid),
                    "stdout": (v.get("exec", {}) or {}).get("stdout", ""),
                })
    return samples


# ---- LLM judge (optional) -------------------------------------------------
JUDGE_SYS = (
    "You are a strict grader for ASE (Atomic Simulation Environment) Python tasks. "
    "Given the TASK, the SUBMITTED CODE, and its STDOUT, decide whether the code "
    "CORRECTLY accomplishes what the task asks — not just whether it ran. Watch for "
    "subtle errors: wrong supercell (e.g. `a*2*2*2` instead of `a*(2,2,2)`), wrong "
    "structure, missing/incorrect printed quantity, hard-coded fake outputs. "
    "Answer with a single JSON object: {\"correct\": true|false, \"reason\": \"<short>\"}."
)


def judge_one(client, model, rec):
    user = (f"TASK ({rec['tid']}, {rec['category']}/{rec['difficulty']}):\n{rec['prompt']}\n"
            f"tests_api: {rec['tests_api']}\n\n"
            f"SUBMITTED CODE:\n```python\n{rec['code'][:4000]}\n```\n\n"
            f"STDOUT:\n{rec['stdout'][:1500]}")
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": JUDGE_SYS},
                  {"role": "user", "content": user}],
        temperature=0.0,
    )
    txt = resp.choices[0].message.content
    try:
        import re
        m = re.search(r"\{.*\}", txt, __import__("re").DOTALL)
        return json.loads(m.group(0))
    except Exception:
        return {"correct": None, "reason": "parse_fail:" + (txt or "")[:120]}


def get_openai_key():
    return subprocess.run(
        ["security", "find-generic-password", "-s", "opencode-openai-api-key", "-w"],
        capture_output=True, text=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5, help="PASS samples per model_cond")
    ap.add_argument("--judge", action="store_true", help="LLM-judge the samples")
    ap.add_argument("--judge-model", default="gpt-4.1-mini")
    args = ap.parse_args()

    samples = collect(args.n)
    print(f"collected {len(samples)} PASS samples "
          f"({len(set((s['alias'], s['cond']) for s in samples))} model_conds)")

    if args.judge:
        from openai import OpenAI
        client = OpenAI(api_key=get_openai_key())
        fp_by_model = {}
        for i, s in enumerate(samples):
            verdict = judge_one(client, args.judge_model, s)
            s["judge"] = verdict
            ok = verdict.get("correct")
            mk = f"{s['alias']}_{s['cond']}"
            fp_by_model.setdefault(mk, [0, 0])
            fp_by_model[mk][1] += 1
            if ok is False:
                fp_by_model[mk][0] += 1
            print(f"  [{i+1}/{len(samples)}] {mk} {s['tid']} -> "
                  f"correct={ok}  {verdict.get('reason','')[:70]}")
        print("\n=== false-positive rate (judged wrong / PASS sampled) ===")
        tot_w = tot_n = 0
        for mk in sorted(fp_by_model):
            w, n = fp_by_model[mk]
            tot_w += w; tot_n += n
            print(f"  {mk:34s} {w}/{n}  ({100*w/n:.0f}% FP)")
        print(f"  {'OVERALL':34s} {tot_w}/{tot_n}  ({100*tot_w/max(tot_n,1):.0f}% FP)")

    with open(OUT_JSON, "w") as f:
        json.dump(samples, f, ensure_ascii=False, indent=1)

    # human-readable md
    lines = [f"# ASE-bench correctness spot-check  (n={args.n}/model_cond, seed={SEED})\n"]
    for s in samples:
        v = s.get("judge", {})
        tag = "" if not v else f"  **judge: correct={v.get('correct')}** — {v.get('reason','')}"
        lines.append(f"\n## {s['alias']} / {s['cond']} / {s['tid']} "
                     f"({s['category']}/{s['difficulty']}){tag}\n")
        lines.append(f"**task:** {s['prompt']}\n")
        lines.append(f"```python\n{s['code']}\n```\n")
        lines.append(f"**stdout:**\n```\n{s['stdout'][:800]}\n```\n")
    with open(OUT_MD, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {OUT_JSON}\nwrote {OUT_MD}")


if __name__ == "__main__":
    main()
