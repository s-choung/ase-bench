"""Re-execute Gemini PASS scripts to capture stdout that the old runner never
stored (benchmark_results.json legacy schema has no stdout field) — so Gemini
was being judged code-only in BOTH judge v1 and v2. Same recapture pattern as
fix_truncated_stdout.py (head 2000 + tail 1500).

- Backs up benchmark_results.json to ~/.archive/<date>/ first (no overwrite).
- For every success==True record of the 6 Gemini conds, runs the script in a
  scratch cwd and stores rec["exec"] = {"returncode", "stdout"(bounded)}.
- Records whose re-run returncode != 0 keep success as originally scored but
  get flagged in the report (env drift / flaky).

Run: conda run -n base python rerun_gemini_stdout.py
"""
import json
import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "results_v3", "benchmark_results.json")
CONDS = ["2.5-pro_vanilla", "2.5-pro_skill_v3", "2.5-flash_vanilla",
         "2.5-flash_skill_v3", "2.5-flash-lite_vanilla", "2.5-flash-lite_skill_v3"]


def bounded(s, head=2000, tail=1500):
    if len(s) <= head + tail:
        return s
    return s[:head] + "\n...[middle truncated]...\n" + s[-tail:]


def run_one(args):
    key, tid, script = args
    cwd = tempfile.mkdtemp(prefix="gem_rerun_")
    try:
        r = subprocess.run(["conda", "run", "-n", "base", "python", script],
                           capture_output=True, text=True, timeout=300, cwd=cwd)
        return key, tid, r.returncode, bounded(r.stdout)
    except subprocess.TimeoutExpired as e:
        return key, tid, -9, bounded((e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""))
    finally:
        shutil.rmtree(cwd, ignore_errors=True)  # scratch only, never repo files


def main():
    arch = os.path.expanduser(f"~/.archive/{date.today()}")
    os.makedirs(arch, exist_ok=True)
    bak = os.path.join(arch, "benchmark_results_pre_gemini_stdout.json")
    if not os.path.exists(bak):
        shutil.copy2(RES, bak)
        print(f"backup -> {bak}")

    data = json.load(open(RES))
    jobs = []
    for key in CONDS:
        for tid, rec in data[key].items():
            if not rec.get("success"):
                continue
            num = tid[1:].zfill(2)
            script = os.path.join(BASE, "generated_v3", key, f"task_{num}.py")
            if os.path.exists(script):
                jobs.append((key, tid, script))
    print(f"{len(jobs)} PASS scripts to re-run")

    drift = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, (key, tid, rc, out) in enumerate(ex.map(run_one, jobs), 1):
            data[key][tid]["exec"] = {"returncode": rc, "stdout": out}
            if rc != 0:
                drift.append((key, tid, rc))
            if i % 20 == 0:
                print(f"  {i}/{len(jobs)} done")

    json.dump(data, open(RES, "w"), ensure_ascii=False, indent=1)
    print(f"wrote stdout for {len(jobs)} records into {RES}")
    if drift:
        print(f"!! {len(drift)} records no longer run clean (env drift; success kept):")
        for d in drift:
            print("  ", d)


if __name__ == "__main__":
    main()
