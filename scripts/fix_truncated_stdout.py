"""Fix the stored-stdout truncation bias.

Bug: runners stored stdout[:2000] (HEAD only). Verbose tasks (NEB/MD: long
BFGS/step logs) lose their FINAL line — which is where the answer is printed —
so the judge cannot verify them and unfairly scores partial/wrong
(e.g. fable-5 T34: code correct, barrier line cut).

Fix: re-run every PASS record whose stored stdout hit the 2000-char cap and
re-store head+tail (head 2000 + tail 1500). Prints the affected
model_cond/tid list so those can be surgically re-judged.

Covers: results_v3/openrouter/*.json (code at generated_v3/eng/<key>/) and
results_v3/benchmark_results_claude.json (code at generated_v3/<key>/).
"""
import glob
import json
import os
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3")


def bounded(s, head=2000, tail=1500):
    if len(s) <= head + tail:
        return s
    return s[:head] + "\n...[middle truncated]...\n" + s[-tail:]


def rerun(script):
    try:
        r = subprocess.run(["conda", "run", "-n", "base", "python", script],
                           capture_output=True, text=True, timeout=300,
                           cwd=os.path.dirname(script))
        return r
    except subprocess.TimeoutExpired:
        return None


def fix_file(path, gen_root):
    j = json.load(open(path))
    affected = []
    for key, res in j.items():
        if not isinstance(res, dict):
            continue
        for tid, v in sorted(res.items()):
            if not isinstance(v, dict):
                continue
            ex = v.get("exec") or {}
            if ex.get("returncode") != 0 or len(ex.get("stdout", "")) < 2000:
                continue
            script = os.path.join(gen_root, key, f"task_{tid[1:].zfill(2)}.py")
            if not os.path.exists(script):
                print(f"  !! no script for {key}/{tid}")
                continue
            r = rerun(script)
            if r is None or r.returncode != 0:
                print(f"  !! rerun failed {key}/{tid} (keeping stored stdout)")
                continue
            ex["stdout"] = bounded(r.stdout)
            affected.append((key, tid))
            print(f"  fixed {key}/{tid} (full stdout {len(r.stdout)} chars)")
    if affected:
        json.dump(j, open(path, "w"), ensure_ascii=False, indent=1)
    return affected


def main():
    all_affected = []
    for f in sorted(glob.glob(os.path.join(RES, "openrouter", "*.json"))):
        all_affected += fix_file(f, os.path.join(BASE, "generated_v3", "eng"))
    all_affected += fix_file(os.path.join(RES, "benchmark_results_claude.json"),
                             os.path.join(BASE, "generated_v3"))
    print(f"\ntotal fixed: {len(all_affected)}")
    by = {}
    for key, tid in all_affected:
        by.setdefault(key, []).append(tid)
    print(json.dumps(by, indent=1))


if __name__ == "__main__":
    main()
