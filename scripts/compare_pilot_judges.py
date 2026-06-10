"""Compare Opus vs Sonnet verdicts from the judge-v2 pilot.

Reads results_v3/judge_out_v2_pilot/{opus,sonnet}__<cond>.json
Prints per-cond agreement, kappa-ish stats, and every disagreement with
both reasons, plus agreement of each judge with the deterministic anchor
(results_v3/correctness.json) where available.
"""
import glob
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")
PILOT = os.path.join(RES, "judge_out_v2_pilot")

D2K = {"Haiku 4.5": "haiku-4-5-20251001", "Sonnet 4.6": "sonnet-4-6", "Opus 4.7": "opus-4-7",
       "pro": "2.5-pro", "flash": "2.5-flash", "flash-lite": "2.5-flash-lite"}


def det_key(cond_name):
    cond = "skill_v3" if cond_name.endswith("_skill_v3") else "vanilla"
    alias = cond_name[: -(len(cond) + 1)]
    return f"{D2K.get(alias, alias)}_{cond}"


def main():
    det = json.load(open(os.path.join(RES, "correctness.json")))
    conds = sorted({os.path.basename(f).split("__", 1)[1][:-5]
                    for f in glob.glob(os.path.join(PILOT, "*__*.json"))})
    tot = agree = hard = 0
    det_match = {"opus": [0, 0], "sonnet": [0, 0]}  # [agree, checkable]
    for k in conds:
        po = os.path.join(PILOT, f"opus__{k}.json")
        ps = os.path.join(PILOT, f"sonnet__{k}.json")
        if not (os.path.exists(po) and os.path.exists(ps)):
            print(f"{k}: missing one side, skip")
            continue
        o = {v["tid"]: v for v in json.load(open(po))["verdicts"]}
        s = {v["tid"]: v for v in json.load(open(ps))["verdicts"]}
        dk = det.get(det_key(k), {})
        n = a = h = 0
        diffs = []
        for tid in sorted(set(o) & set(s), key=lambda t: int(t[1:])):
            vo, vs = o[tid]["verdict"], s[tid]["verdict"]
            n += 1
            if vo == vs:
                a += 1
            else:
                if abs(vo - vs) == 2:
                    h += 1
                diffs.append((tid, vo, vs, o[tid]["reason"][:70], s[tid]["reason"][:70]))
            dv = (dk.get(tid) or {}).get("verdict")
            if dv in (0, 2):
                for tag, v in (("opus", vo), ("sonnet", vs)):
                    det_match[tag][1] += 1
                    # judge 1 (partial) counts as agreeing with det 2 but not det 0
                    jbin = 2 if v >= 1 else 0
                    if jbin == dv:
                        det_match[tag][0] += 1
        tot += n
        agree += a
        hard += h
        print(f"{k}: {a}/{n} agree ({100*a/max(n,1):.0f}%), hard(2v0)={h}")
        for d in diffs:
            print(f"   {d[0]}: opus={d[1]} sonnet={d[2]}\n      O: {d[3]}\n      S: {d[4]}")
    print(f"\nOVERALL agreement: {agree}/{tot} = {100*agree/max(tot,1):.0f}% | hard disagreements: {hard}")
    for tag, (m, c) in det_match.items():
        print(f"{tag} vs deterministic anchor: {m}/{c} = {100*m/max(c,1):.0f}%")


if __name__ == "__main__":
    main()
