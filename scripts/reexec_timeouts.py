"""Re-execute ONLY the tasks that failed with a TIMEOUT (returncode -1, stderr
'TIMEOUT') in the 8 KO->EN re-run models. Those are false-negatives from CPU
oversubscription during concurrent generation (load ~38/8 cores), not real
code failures. The generated .py already exists, so we just re-run it locally
under low load with the SAME 60s budget (methodology parity with the board).
Updates results_v3/openrouter/<alias>.json in place. No API calls.
"""
import json
import os
import subprocess
import time

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3", "openrouter")
GEN = os.path.join(BASE, "generated_v3", "eng")
ALIASES = ["claude-fable-5", "claude-haiku-4.5", "claude-opus-4.7", "claude-opus-4.8",
           "claude-sonnet-4.6", "gemini-2.5-pro", "gemini-2.5-flash", "gemini-2.5-flash-lite"]
CONDS = ["vanilla", "skill_v3"]


def run_script(fp, timeout=60):
    start = time.time()
    try:
        r = subprocess.run(["conda", "run", "-n", "base", "python", fp],
                           capture_output=True, text=True, timeout=timeout,
                           cwd=os.path.dirname(fp))
        out = r.stdout if len(r.stdout) <= 3500 else (
            r.stdout[:2000] + "\n...[middle truncated]...\n" + r.stdout[-1500:])
        return {"success": r.returncode == 0, "returncode": r.returncode, "stdout": out,
                "stderr": r.stderr[:2000], "elapsed": round(time.time() - start, 3)}
    except subprocess.TimeoutExpired:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": "TIMEOUT",
                "elapsed": timeout}
    except Exception as e:
        return {"success": False, "returncode": -1, "stdout": "", "stderr": str(e),
                "elapsed": round(time.time() - start, 3)}


def main():
    recovered = still = 0
    for alias in ALIASES:
        path = os.path.join(RES, f"{alias}.json")
        j = json.load(open(path))
        changed = False
        for cond in CONDS:
            key = f"{alias}_{cond}"
            recs = j.get(key, {})
            for tid, r in recs.items():
                ex = r.get("exec", {}) or {}
                if (ex.get("stderr", "") or "").strip() != "TIMEOUT":
                    continue
                num = tid[1:].zfill(2)
                fp = os.path.join(GEN, key, f"task_{num}.py")
                if not os.path.exists(fp):
                    print(f"  {key} {tid}: .py missing, skip")
                    continue
                newex = run_script(fp)
                r["exec"] = newex
                r["success"] = newex["success"]
                changed = True
                if newex["success"]:
                    recovered += 1
                    tag = "RECOVERED"
                else:
                    still += 1
                    tag = "still " + ((newex["stderr"] or "").strip().split("\n")[-1][:40])
                print(f"  {key} {tid}: {tag} ({newex['elapsed']:.1f}s)")
        if changed:
            json.dump(j, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"\nDONE: recovered={recovered}  still-fail={still}")


if __name__ == "__main__":
    main()
