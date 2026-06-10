"""Build judge_inputs/<model_cond>.json for model_conds that have no Opus
verdicts yet. One file per model_cond, PASS (returncode==0) tasks only —
same schema as the 2026-06-09 judge run:
  {model_cond, tasks: [{tid, prompt, category, difficulty, tests_api, code, stdout}]}

Usage:
  python build_judge_inputs.py <alias> [...]   # openrouter aliases and/or 'fable-5'
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OUTDIR = os.path.join(RES, "judge_inputs")

PROMPTS = {t["id"]: t for t in json.load(open(os.path.join(BASE, "prompts_50_eng.json")))["tasks"]}
PROMPTS_KO = {t["id"]: t for t in json.load(open(os.path.join(BASE, "prompts_50.json")))["tasks"]}


def code_path(key, tid, eng):
    num = tid[1:].zfill(2)
    sub = os.path.join("generated_v3", "eng", key) if eng else os.path.join("generated_v3", key)
    return os.path.join(BASE, sub, f"task_{num}.py")


def build_one(key, records, eng):
    tasks = []
    for tid in sorted(records, key=lambda t: int(t[1:])):
        r = records[tid]
        ex = r.get("exec") or {}
        if ex.get("returncode") != 0:
            continue
        cp = code_path(key, tid, eng)
        code = open(cp).read() if os.path.exists(cp) else ""
        ref = (PROMPTS if eng else PROMPTS_KO).get(tid, {})
        tasks.append({
            "tid": tid,
            "prompt": r.get("prompt", ref.get("prompt", "")),
            "category": r.get("category", ref.get("category", "")),
            "difficulty": r.get("difficulty", ref.get("difficulty", "")),
            "tests_api": ref.get("tests_api", ""),
            "code": code,
            "stdout": ex.get("stdout", ""),
        })
    out = os.path.join(OUTDIR, f"{key}.json")
    json.dump({"model_cond": key, "tasks": tasks}, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"{key}: {len(tasks)} PASS tasks -> {out}")


def main():
    for alias in sys.argv[1:]:
        if alias == "fable-5":
            j = json.load(open(os.path.join(RES, "benchmark_results_claude.json")))
            for cond in ["vanilla", "skill_v3"]:
                key = f"fable-5_{cond}"
                build_one(key, j[key], eng=False)
        else:
            j = json.load(open(os.path.join(RES, "openrouter", f"{alias}.json")))
            for key, records in sorted(j.items()):
                build_one(key, records, eng=True)


if __name__ == "__main__":
    main()
