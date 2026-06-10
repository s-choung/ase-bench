"""Surgical judge-v2 fix inputs after the 2026-06-10 rubric corrections
(T37 opt-variant Gibbs refs, T40 P1-after-CIF quirk, T46 bond-preservation
criterion, T48 self-distance partial rule).

Selects (cond, tid) where tid in {T37,T40,T46,T48} and the CURRENT v2 verdict
is < 2 (corrections only relax), excluding the 6 Gemini conds (those get a
full re-judge with their newly captured stdout). Writes
results_v3/judge_inputs_v2_fix/<cond>.json with only those task entries.

Run: conda run -n base python build_fix_inputs_v2.py
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OUT = os.path.join(RES, "judge_inputs_v2_fix")
os.makedirs(OUT, exist_ok=True)

TIDS = {"T37", "T40", "T46", "T48"}
GEMINI = {"pro_vanilla", "pro_skill_v3", "flash_vanilla", "flash_skill_v3",
          "flash-lite_vanilla", "flash-lite_skill_v3"}

conds = []
for f in sorted(glob.glob(os.path.join(RES, "judge_out_v2", "*.json"))):
    name = os.path.basename(f)[:-5]
    if name in GEMINI:
        continue
    tids = [v["tid"] for v in json.load(open(f))["verdicts"]
            if v["tid"] in TIDS and v["verdict"] is not None and v["verdict"] < 2]
    if not tids:
        continue
    ji = json.load(open(os.path.join(RES, "judge_inputs_v2", f"{name}.json")))
    tasks = [t for t in ji["tasks"] if t["tid"] in tids]
    json.dump({"model_cond": name, "rules": ji["rules"], "tasks": tasks},
              open(os.path.join(OUT, f"{name}.json"), "w"), ensure_ascii=False, indent=1)
    conds.append(name)
    print(f"{name}: {sorted(tids)}")
print(f"\n{len(conds)} fix files -> {OUT}")
print(json.dumps(conds))
