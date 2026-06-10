"""Extract a representative atomic structure for each of the 50 ASE tasks by
running GPT-5.5's (skill_v3, 50/50 PASS) generated code and dumping the main
ase.Atoms object to XYZ. Feeds the Task Visualizer gallery (so the abstract
task list becomes a visual 5x10 grid of what each task builds).

Method: for each task, write a wrapper = [preamble that stubs GUI/plot] +
[the model's code] + [epilogue that scans globals() for Atoms and writes the
largest one to structures/<tid>.xyz]. Run as an isolated subprocess (conda
base) in a scratch cwd with a timeout, so trajectory/db side-files don't
pollute and GUI calls can't hang.
"""
import json
import os
import re
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(BASE, "benchmark_report_v8.html")
OUT = os.path.join(BASE, "structures")
SCRATCH = os.path.join(BASE, "structures", "_scratch")
KEY = "gpt-5.5_skill_v3"

PREAMBLE = (
    "import matplotlib\nmatplotlib.use('Agg')\n"
    "import warnings; warnings.filterwarnings('ignore')\n"
    "try:\n import ase.visualize as _vis\n _vis.view=lambda *a,**k:None\nexcept Exception:\n pass\n"
)
EPILOGUE = '''
def _dump_structure(_path):
    try:
        from ase import Atoms as _A
        from ase.io import write as _w
        g = dict(globals())
        cands = [v for v in g.values() if isinstance(v, _A) and len(v) > 0]
        for v in g.values():
            if isinstance(v, (list, tuple)) and v and all(isinstance(x, _A) for x in v):
                cands.append(max(v, key=len))
        if not cands:
            print("XYZ_NONE"); return
        best = max(cands, key=lambda a: len(a))
        # ensure a cell for molecules so the viewer frames sensibly
        _w(_path, best)
        print("XYZ_WROTE", len(best), best.get_chemical_formula())
    except Exception as _e:
        print("XYZ_FAIL", repr(_e))

_dump_structure(__OUT_XYZ__)
'''


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(SCRATCH, exist_ok=True)
    h = open(V8).read()
    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))
    tids = sorted(DATA, key=lambda t: int(t[1:]))

    ok = []
    for tid in tids:
        m = DATA[tid]["models"].get(KEY, {})
        code = m.get("code", "")
        if not code:
            print(f"{tid}: no code"); continue
        xyz = os.path.join(OUT, f"{tid}.xyz")
        wrapper = (PREAMBLE + "\n" + code + "\n" +
                   EPILOGUE.replace("__OUT_XYZ__", repr(xyz)))
        wf = os.path.join(SCRATCH, f"{tid}.py")
        with open(wf, "w") as f:
            f.write(wrapper)
        try:
            r = subprocess.run(["conda", "run", "-n", "base", "python", wf],
                               capture_output=True, text=True, timeout=120, cwd=SCRATCH)
            tail = [l for l in (r.stdout + r.stderr).splitlines() if "XYZ_" in l]
            msg = tail[-1] if tail else (r.stderr.strip().splitlines() or ["?"])[-1][:80]
        except subprocess.TimeoutExpired:
            msg = "TIMEOUT"
        got = os.path.exists(xyz)
        if got:
            ok.append(tid)
        print(f"{tid}: {'OK ' if got else 'MISS'} {msg}")

    print(f"\nextracted {len(ok)}/{len(tids)} structures -> {OUT}")
    print("missing:", [t for t in tids if t not in ok])


if __name__ == "__main__":
    main()
