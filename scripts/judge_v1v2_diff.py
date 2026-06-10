"""Diff judge v1 (judge_out/, Opus generic rubric) vs v2 (judge_out_v2/,
Sonnet + per-task explicit rubrics).

Reports:
  - per-task verdict-change counts (which tasks flipped most, direction)
  - per-model correct-count change (leaderboard impact, w/ skill cond)
  - rubric_conflict cases (need human review)
  - headline check: fable-5 / gpt-5.5 correct counts v1 vs v2

Usage: python judge_v1v2_diff.py
Writes results_v3/judge_v1v2_diff.json
"""
import glob
import json
import os
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")


def load(d):
    out = {}
    for f in glob.glob(os.path.join(RES, d, "*.json")):
        name = os.path.basename(f)[:-5]
        if name.startswith("fix__"):
            continue
        j = json.load(open(f))
        out[name] = {v["tid"]: v for v in j["verdicts"]}
    return out


def main():
    v1 = load("judge_out")
    v2 = load("judge_out_v2")
    common = sorted(set(v1) & set(v2))
    print(f"v1 conds: {len(v1)} | v2 conds: {len(v2)} | common: {len(common)}")
    missing_v2 = sorted(set(v1) - set(v2))
    if missing_v2:
        print("!! not yet in v2:", missing_v2)

    task_flip = defaultdict(Counter)   # tid -> "v1->v2" -> n
    model_corr = {}                    # cond -> (v1_correct, v2_correct)
    conflicts = []
    n_same = n_diff = 0
    for k in common:
        c1 = sum(1 for v in v1[k].values() if v["verdict"] == 2)
        c2 = sum(1 for v in v2[k].values() if v["verdict"] == 2)
        model_corr[k] = (c1, c2)
        for tid in set(v1[k]) & set(v2[k]):
            a, b = v1[k][tid]["verdict"], v2[k][tid]["verdict"]
            if a == b:
                n_same += 1
            else:
                n_diff += 1
                task_flip[tid][f"{a}->{b}"] += 1
            if v2[k][tid].get("rubric_conflict"):
                conflicts.append({"cond": k, "tid": tid,
                                  "reason": v2[k][tid].get("reason", "")})

    print(f"\nverdicts same {n_same} / changed {n_diff} "
          f"({100*n_diff/max(n_same+n_diff,1):.0f}% changed)")
    print("\n-- most-flipped tasks --")
    for tid, c in sorted(task_flip.items(), key=lambda x: -sum(x[1].values()))[:15]:
        print(f"  {tid}: {sum(c.values()):3d}  {dict(c)}")
    print("\n-- biggest leaderboard moves (w/ skill correct count) --")
    moves = sorted(model_corr.items(), key=lambda x: -abs(x[1][1] - x[1][0]))
    for k, (a, b) in moves[:15]:
        print(f"  {k:36s} {a:3d} -> {b:3d}  ({b-a:+d})")
    print("\n-- headline models --")
    for k in ["fable-5_vanilla", "fable-5_skill_v3", "gpt-5.5_vanilla", "gpt-5.5_skill_v3"]:
        if k in model_corr:
            a, b = model_corr[k]
            print(f"  {k}: {a} -> {b}")
    print(f"\n-- rubric_conflict flags: {len(conflicts)} --")
    for c in conflicts[:20]:
        print(f"  {c['cond']} {c['tid']}: {c['reason'][:90]}")

    json.dump({"model_corr": {k: list(v) for k, v in model_corr.items()},
               "task_flips": {t: dict(c) for t, c in task_flip.items()},
               "rubric_conflicts": conflicts,
               "n_same": n_same, "n_diff": n_diff},
              open(os.path.join(RES, "judge_v1v2_diff.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\nwrote {os.path.join(RES, 'judge_v1v2_diff.json')}")


if __name__ == "__main__":
    main()
