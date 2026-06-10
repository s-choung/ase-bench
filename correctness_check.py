"""Deterministic CORRECTNESS check for the 50-task ASE bench.

The harness records success = (returncode == 0) = "does it RUN". An LLM-judge
spot-check showed ~52% of those PASSes are actually WRONG (wrong supercell,
wrong layer/atom count, NaN cell, complex frequencies, ...). So "runs" badly
overstates competence. This script adds a *deterministic, reproducible,
free* correctness layer by parsing the SAVED stdout (no re-execution, no API)
and checking task-specific invariant facts.

Method = "required-fact presence". For each task we curated the canonical
observable(s) — atom counts, chemical formula, cell edge, volume, key
distances, coordination number — computed from a reference ASE build (see
HANDOVER). A model's stdout is CORRECT if it contains every required fact
(integers exact; floats within tol; strings as substrings), with alternative
fact-sets allowed where the prompt is genuinely ambiguous (e.g. T01 a 2x2x2
supercell is 8 atoms primitive or 32 conventional — both defensible).

Tasks whose correct answer is not a clean checkable fact (most energy / MD /
NEB / vibration / thermo tasks) are marked `indeterminate` — we do NOT claim
correctness for them; the report shows them separately and falls back to the
runs signal. This is honest: structural FPs (the bulk of what the judge
caught) are checked; numeric-physics FPs await a deterministic-energy pass.

verdict per (model, cond, task):  2 = correct, 0 = wrong, -1 = indeterminate,
                                  None = did not run (no PASS to judge)

Reads:
  results_v3/openrouter/<alias>.json          (13 open models)
  results_v3/benchmark_results_openai_eng.json (OpenAI closed)
  results_v3/benchmark_results_claude.json      (Claude closed)
  results_v3/benchmark_results.json             (Gemini closed)
Writes:
  results_v3/correctness.json   { "<alias>_<cond>": { tid: {verdict, why} } }
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
OPENROUTER = os.path.join(RES, "openrouter")
OUT = os.path.join(RES, "correctness.json")

CONDS = ["vanilla", "skill_v3"]

# closed-model result files (dict keyed "<model>_<cond>" -> {tid: {success, exec:{stdout}}})
CLOSED_FILES = [
    "benchmark_results_openai_eng.json",
    "benchmark_results_claude.json",
    "benchmark_results.json",  # gemini (+ maybe others)
]

# --------------------------------------------------------------------- spec ---
# fact kinds:
#   ("int", v)         exact integer v must appear as a standalone number
#   ("near", v, tol)   some number within tol of v
#   ("sub", s)         lowercased substring s must appear
#   ("bad", s)         lowercased substring s must NOT appear (else wrong)
# A task spec is a list of "alternatives"; the verdict is correct if ANY
# alternative has ALL its facts satisfied. `bad` facts apply across all alts.
# NOTE on calibration (judge-the-judge findings, 2026-06-09): the first cut of
# this spec over-keyed on facts the prompt did not request (T03 asks only for
# cell size, T12 for vectors/positions, T18 for coords/formula — not atom
# count) and used a couple of wrong reference values (T17 surface(2,1,1) layers=3
# is 3 atoms, not 12; T40 CIF round-trip can return the 2-atom primitive). The
# N2/H2O/CH4 vib "no-complex" check was also wrong: ASE prints near-zero
# IMAGINARY trans/rot modes as a matter of course; only the physical stretch
# must be real. Those tasks were removed/loosened so the deterministic layer is
# a TRUSTWORTHY anchor (it only fires where the prompt explicitly asks for the
# checked fact and the reference value is unambiguous). Opus was right in every
# one of those conflicts — see results_v3/correctness_audit.html.
# v2 EXTENSION (2026-06-10, judge-v2 work): new entries below are sourced from
# results_v3/reference_facts.json — values COMPUTED with ASE/EMT in this exact
# env (reference_facts.py), not guessed. Same calibration principle as v1:
# only facts the prompt explicitly asks for; alts for genuinely ambiguous
# builds. Key probe finding: T17 surface("Cu",(2,1,1),3) string-lattice gives
# 12 atoms and add_vacuum() then produces a NAN cell row — ASE behavior under
# literal prompt compliance, so nan is NOT penalized and 3 (primitive bulk
# form) and 12 (string/cubic form) atoms are BOTH correct.
SPEC = {
    "T01": {"alts": [[("int", 8)], [("int", 32)]], "why": "Cu fcc 2x2x2 = 8 (prim) or 32 (conv) atoms"},
    "T03": {"alts": [[("near", 3.18, 0.02)]],
            "why": "MoS2 monolayer a=3.18 (prompt asks cell size; c free via vacuum)"},
    "T04": {"alts": [[("near", 1.8793, 0.04)]],
            "why": "EMT H2O optimized energy ~1.879 (universal EMT minimum; initial geometry "
                   "is the model's choice so e_before is free)"},
    "T05": {"alts": [[("near", 11.567, 0.3), ("near", 133.6, 8.0)],
                     [("near", 46.27, 1.2), ("near", 133.6, 8.0)],
                     [("near", 11.567, 0.3), ("near", 0.834, 0.05)],
                     [("near", 46.27, 1.2), ("near", 0.834, 0.05)]],
            "bad": [("near", 2.26, 0.025)],
            "why": "Cu EOS: V0 11.57/atom (46.3/conv cell) + B 133.6 GPa (0.834 eV/A^3); "
                   "2.26 = v0^(1/3) mistaken for a lattice constant -> wrong"},
    "T12": {"alts": [[("near", 2.95, 0.001), ("near", 4.6905, 0.01)]],
            "why": "Ti hcp a=2.95, c=4.6905 in printed cell vectors"},
    "T17": {"alts": [[("int", 12)], [("int", 3)]],
            "why": "surface(Cu,(2,1,1),3): 12 atoms (string/cubic lattice) or 3 (primitive); "
                   "nan cell NOT penalized (ASE add_vacuum behavior)"},
    "T25": {"alts": [[("near", 3.589, 0.03)], [("near", 2.538, 0.02)]],
            "why": "Cu cell-opt eq lattice 3.589 conv (2.538 prim edge)"},
    "T36": {"alts": [[("near", 4.0636, 0.04), ("near", 99.8, 8.0)]],
            "why": "Ag EOS eq a 4.064 + B 99.8 GPa (prompt asks both, GPa explicit)"},
    "T50": {"alts": [[("near", 3.59, 0.04), ("near", 4.0636, 0.04), ("near", 4.0562, 0.04)]],
            "why": "Cu/Ag/Au EOS table: eq lattice constants 3.59 / 4.064 / 4.056"},
    "T10": {"alts": [[("int", 85)]], "why": "Cu Octahedron(length=5) = 85 atoms"},
    "T11": {"alts": [[("int", 2), ("sub", "al2")], [("int", 2), ("near", 3.3, 0.001)]],
            "why": "Al bcc cubic = 2 atoms (Al2), cell edge 3.3 (prompt asks cell + formula)"},
    "T13": {"alts": [[("int", 216), ("near", 4322.78, 5.0)], [("int", 54), ("near", 1080.7, 3.0)],
                     [("int", 216)], [("int", 54)]],
            "why": "Si diamond 3x3x3 = 216 (conv) or 54 (prim) atoms (prompt asks atoms + volume)"},
    "T14": {"alts": [[("int", 8), ("sub", "na")], [("int", 8)]], "why": "NaCl sg225 = 8 atoms (prompt asks atoms + symbols)"},
    "T15": {"alts": [[("int", 27)]], "why": "Cu(100) size=(3,3,3) = 27 atoms (prompt asks atoms)"},
    "T16": {"alts": [[("int", 16)], [("int", 32)]], "why": "Fe bcc110 size=(2,2,4) = 16 atoms (32 if doubled cell)"},
    "T18": {"alts": [[("sub", "ch4")]], "why": "CH4 formula (prompt asks coords/bonds/formula, not count)"},
    "T19": {"alts": [[("near", 1.16, 0.02), ("near", 2.32, 0.03)]], "why": "CO2 distances 1.16 & 2.32"},
    "T20": {"alts": [[("int", 96)], [("int", 144)], [("int", 240)]],
            "why": "(6,6) CNT length=4 = 96 atoms (length convention varies)"},
    "T21": {"alts": [[("int", 55)]], "why": "Au Icosahedron(noshells=3) = 55 atoms (prompt asks atoms)"},
    "T47": {"alts": [[("int", 108), ("near", 12.0, 0.3)], [("near", 12.0, 0.3)]],
            "why": "Cu fcc 3x3x3 avg coordination = 12 (prompt asks avg CN)"},
}
# every other task -> indeterminate (not deterministically checkable here)

NUM_RE = re.compile(r"-?\d+\.?\d*(?:[eE][-+]?\d+)?")


def numbers(text):
    out = []
    for tok in NUM_RE.findall(text):
        try:
            out.append(float(tok))
        except ValueError:
            pass
    return out


def fact_ok(fact, nums, low):
    k = fact[0]
    if k == "int":
        return any(abs(n - fact[1]) < 1e-9 for n in nums)
    if k == "near":
        return any(abs(n - fact[1]) <= fact[2] for n in nums)
    if k == "sub":
        return fact[1] in low
    return False


def judge(tid, stdout):
    spec = SPEC.get(tid)
    if spec is None:
        return -1, "indeterminate (no deterministic check)"
    low = stdout.lower()
    nums = numbers(stdout)
    # hard-fail signals: substrings, or ("near", v, tol) wrong-derivation values
    for b in spec.get("bad", []):
        if isinstance(b, str):
            if b in low:
                return 0, f"contains '{b}' (bad signal)"
        elif fact_ok(b, nums, low):
            return 0, f"bad value ~{b[1]} present (wrong derivation): " + spec["why"]
    alts = spec.get("alts", [])
    if not alts:  # only a bad-check task (e.g. vib); passing the bad-check = correct
        return 2, spec["why"] + " — ok"
    for alt in alts:
        if all(fact_ok(f, nums, low) for f in alt):
            return 2, spec["why"]
    return 0, "required fact(s) missing: " + spec["why"]


# ------------------------------------------------------------------- loaders ---
def rec_stdout(v):
    if not isinstance(v, dict):
        return None
    if "exec" in v and isinstance(v["exec"], dict):
        return v["exec"].get("stdout", "")
    return v.get("stdout", "")


def collect():
    """-> { model_cond: { tid: {success, stdout} } }  for all 22 models."""
    data = {}
    # open models
    import glob
    for f in glob.glob(os.path.join(OPENROUTER, "*.json")):
        alias = os.path.basename(f)[:-5]
        r = json.load(open(f))
        for cond in CONDS:
            key = f"{alias}_{cond}"
            d = r.get(key)
            if not d:
                continue
            data[key] = {tid: {"success": bool(v.get("success")), "stdout": rec_stdout(v) or ""}
                         for tid, v in d.items()}
    # closed models
    for fn in CLOSED_FILES:
        fp = os.path.join(RES, fn)
        if not os.path.exists(fp):
            continue
        r = json.load(open(fp))
        for key, d in r.items():
            if not isinstance(d, dict):
                continue
            if key in data:  # don't clobber
                continue
            data[key] = {tid: {"success": bool(v.get("success")), "stdout": rec_stdout(v) or ""}
                         for tid, v in d.items() if isinstance(v, dict)}
    return data


def main():
    data = collect()
    out = {}
    # tallies
    from collections import defaultdict
    tally = defaultdict(lambda: {"run": 0, "correct": 0, "wrong": 0, "indet": 0})
    for key, tasks in data.items():
        out[key] = {}
        for tid, rec in tasks.items():
            if not rec["success"]:
                out[key][tid] = {"verdict": None, "why": "did not run"}
                continue
            v, why = judge(tid, rec["stdout"])
            out[key][tid] = {"verdict": v, "why": why}
            tally[key]["run"] += 1
            if v == 2:
                tally[key]["correct"] += 1
            elif v == 0:
                tally[key]["wrong"] += 1
            else:
                tally[key]["indet"] += 1

    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    # report: among CHECKABLE (correct+wrong), how many wrong = deterministic FP rate
    print(f"{'model_cond':36s} {'runs':>5s} {'corr':>5s} {'wrong':>6s} {'indet':>6s}  FP%(checkable)")
    tw = tc = 0
    for key in sorted(tally):
        t = tally[key]
        chk = t["correct"] + t["wrong"]
        fp = 100 * t["wrong"] / chk if chk else 0
        tw += t["wrong"]; tc += chk
        print(f"{key:36s} {t['run']:>5d} {t['correct']:>5d} {t['wrong']:>6d} {t['indet']:>6d}  "
              f"{fp:>5.0f}% ({chk} chk)")
    print(f"\nOVERALL deterministic FP rate (wrong / checkable PASS): "
          f"{tw}/{tc} = {100*tw/max(tc,1):.0f}%")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
