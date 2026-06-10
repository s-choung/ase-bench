"""Merge the uniform T22 group verdicts (judge_out_v2_t22/group_*.json)
into canonical judge_out_v2/<cond>.json.

Run: conda run -n base python merge_t22_v2.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")

new = {}
for f in glob.glob(os.path.join(RES, "judge_out_v2_t22", "group_*.json")):
    for v in json.load(open(f))["verdicts"]:
        new[v["cond"]] = v

n_changed = 0
for cond, v in sorted(new.items()):
    path = os.path.join(RES, "judge_out_v2", f"{cond}.json")
    tj = json.load(open(path))
    for rec in tj["verdicts"]:
        if rec["tid"] == "T22":
            if rec["verdict"] != v["verdict"]:
                print(f"{cond}: {rec['verdict']} -> {v['verdict']} | {v['reason'][:70]}")
                n_changed += 1
            rec["verdict"] = v["verdict"]
            rec["reason"] = v["reason"]
    json.dump(tj, open(path, "w"), ensure_ascii=False, indent=1)
print(f"\n{len(new)} conds merged, {n_changed} verdicts changed")
