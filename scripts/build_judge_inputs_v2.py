"""Build judge v2 inputs: v1 judge_inputs + per-task rubric injection + stdout
refreshed from canonical results (so the 2026-06-10 truncation fixes are in).

For every results_v3/judge_inputs/<name>.json (skipping fix__*):
  - map display name -> canonical results key (Claude display names, old
    Gemini aliases) and pull the CURRENT stdout for each PASS task
  - inject task["rubric"] from judge_rubrics_50.json and the global _rules
  - write results_v3/judge_inputs_v2/<name>.json   (v1 inputs untouched)

Usage: python build_judge_inputs_v2.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OUTDIR = os.path.join(RES, "judge_inputs_v2")
os.makedirs(OUTDIR, exist_ok=True)

RUBRICS = json.load(open(os.path.join(BASE, "judge_rubrics_50.json")))
RULES = RUBRICS.pop("_rules")

# judge_inputs display alias -> results key alias
DISPLAY2KEY = {
    "Haiku 4.5": "haiku-4-5-20251001",
    "Sonnet 4.6": "sonnet-4-6",
    "Opus 4.7": "opus-4-7",
    "pro": "2.5-pro",
    "flash": "2.5-flash",
    "flash-lite": "2.5-flash-lite",
}


def split_key(key):
    cond = "skill_v3" if key.endswith("_skill_v3") else "vanilla"
    return key[: -(len(cond) + 1)], cond


def collect_results():
    """all canonical records: {model_cond_key: {tid: record}}"""
    data = {}
    for f in glob.glob(os.path.join(RES, "openrouter", "*.json")):
        try:
            j = json.load(open(f))
        except json.JSONDecodeError:
            print(f"!! skipping mid-write file: {os.path.basename(f)}")
            continue
        for key, recs in j.items():
            data[key] = recs
    for fn in ["benchmark_results_claude.json", "benchmark_results_openai_eng.json",
               "benchmark_results.json"]:
        fp = os.path.join(RES, fn)
        if not os.path.exists(fp):
            continue
        for key, recs in json.load(open(fp)).items():
            if isinstance(recs, dict):
                data.setdefault(key, recs)
    return data


def main():
    all_res = collect_results()
    n_files = n_refreshed = n_stale = 0
    missing_keys = []
    for f in sorted(glob.glob(os.path.join(RES, "judge_inputs", "*.json"))):
        name = os.path.basename(f)[:-5]
        if name.startswith("fix__"):
            continue
        ji = json.load(open(f))
        alias, cond = split_key(name)
        rkey = f"{DISPLAY2KEY.get(alias, alias)}_{cond}"
        recs = all_res.get(rkey)
        if recs is None:
            missing_keys.append((name, rkey))
        tasks = []
        for t in ji["tasks"]:
            t = dict(t)
            rec = (recs or {}).get(t["tid"]) or {}
            ex = rec.get("exec")
            fresh = ex.get("stdout") if isinstance(ex, dict) else rec.get("stdout")
            if fresh is not None and fresh != t.get("stdout"):
                t["stdout"] = fresh
                n_refreshed += 1
            elif fresh is None:
                n_stale += 1
            t["rubric"] = RUBRICS[t["tid"]]
            tasks.append(t)
        out = {"model_cond": name, "rules": RULES, "tasks": tasks}
        json.dump(out, open(os.path.join(OUTDIR, f"{name}.json"), "w"),
                  ensure_ascii=False, indent=1)
        n_files += 1
    print(f"wrote {n_files} files to {OUTDIR}")
    print(f"stdout refreshed: {n_refreshed} | no canonical stdout found: {n_stale}")
    if missing_keys:
        print("!! unmapped model_conds (kept v1 stdout):")
        for n, k in missing_keys:
            print("  ", n, "->", k)


if __name__ == "__main__":
    main()
