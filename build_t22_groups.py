"""Group inputs for the uniform T22 re-judge (crisped bridge-site decision
rule). Collects every cond's T22 entry from judge_inputs_v2 and chunks them
into groups of 15 -> results_v3/judge_inputs_v2_t22/group_<n>.json

Run: conda run -n base python build_t22_groups.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OUT = os.path.join(RES, "judge_inputs_v2_t22")
os.makedirs(OUT, exist_ok=True)

RUBRIC = json.load(open(os.path.join(BASE, "judge_rubrics_50.json")))["T22"]

entries = []
rules = None
for f in sorted(glob.glob(os.path.join(RES, "judge_inputs_v2", "*.json"))):
    ji = json.load(open(f))
    rules = ji["rules"]
    for t in ji["tasks"]:
        if t["tid"] == "T22":
            t = dict(t)
            t["rubric"] = RUBRIC  # updated rubric
            entries.append({"cond": ji["model_cond"], "task": t})

groups = [entries[i:i + 15] for i in range(0, len(entries), 15)]
for n, g in enumerate(groups, 1):
    json.dump({"rules": rules, "entries": g},
              open(os.path.join(OUT, f"group_{n}.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(entries)} T22 entries -> {len(groups)} groups in {OUT}")
