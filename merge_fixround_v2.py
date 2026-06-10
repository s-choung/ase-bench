"""Merge surgical fix-round verdicts (judge_out_v2_fixround/<cond>.json,
only T37/T40/T46/T48 entries) into the canonical judge_out_v2/<cond>.json.

Gemini conds are NOT touched here (their full files were rewritten in place
by the workflow). fixround files live in their own directory, so the
judge_out aux-file clobber trap does not apply — nothing to archive.

Run: conda run -n base python merge_fixround_v2.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")

n_changed = 0
for f in sorted(glob.glob(os.path.join(RES, "judge_out_v2_fixround", "*.json"))):
    name = os.path.basename(f)[:-5]
    fix = {v["tid"]: v for v in json.load(open(f))["verdicts"]}
    tgt_path = os.path.join(RES, "judge_out_v2", f"{name}.json")
    tj = json.load(open(tgt_path))
    for v in tj["verdicts"]:
        if v["tid"] in fix:
            new = fix[v["tid"]]
            if new["verdict"] != v["verdict"]:
                print(f"{name}/{v['tid']}: {v['verdict']} -> {new['verdict']} | {new['reason'][:70]}")
                n_changed += 1
            v.update(new)
    json.dump(tj, open(tgt_path, "w"), ensure_ascii=False, indent=1)
print(f"\n{n_changed} verdicts changed")
