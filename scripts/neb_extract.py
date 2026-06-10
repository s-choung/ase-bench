"""Re-extract NEB tasks (T34, T35) as an OVERLAY of the band images: concatenate
every image in the band into one Atoms so the moving atom appears as a trail
along the diffusion path (static slab atoms just overlap). Renders then show the
full path in one frame. Uses gpt-5.5 skill_v3 code, falling back to vanilla when
skill_v3 code is empty (T34)."""
import json
import os
import re
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
V8 = os.path.join(BASE, "benchmark_report_v8.html")
OUT = os.path.join(BASE, "structures")
SCRATCH = os.path.join(BASE, "structures", "_scratch")

PREAMBLE = (
    "import matplotlib\nmatplotlib.use('Agg')\n"
    "import warnings; warnings.filterwarnings('ignore')\n"
    "try:\n import ase.visualize as _vis\n _vis.view=lambda *a,**k:None\nexcept Exception:\n pass\n"
)
EPILOGUE = '''
def _dump_overlay(_path):
    try:
        from ase import Atoms as _A
        from ase.io import write as _w
        g = dict(globals())
        bands = [v for v in g.values()
                 if isinstance(v, (list, tuple)) and len(v) >= 3
                 and all(isinstance(x, _A) for x in v)]
        if not bands:
            print("NEB_NONE"); return
        band = max(bands, key=len)
        combined = band[0].copy()
        for img in band[1:]:
            combined += img
        combined.set_pbc(False)
        _w(_path, combined)
        print("NEB_WROTE", len(band), "images ->", len(combined), "atoms")
    except Exception as _e:
        print("NEB_FAIL", repr(_e))

_dump_overlay(__OUT_XYZ__)
'''


def main():
    h = open(V8).read()
    DATA = json.loads(re.search(r"const DATA = (\{.*?\});\s*\n", h, re.S).group(1))
    for tid in ("T34", "T35"):
        m = DATA[tid]["models"]
        code = ""
        for mk in ("gpt-5.5_skill_v3", "gpt-5.5_vanilla", "gpt-5.4_skill_v3",
                   "Opus 4.7_skill_v3", "minimax-m3_skill_v3"):
            code = (m.get(mk, {}).get("code", "") or "").strip()
            if code:
                print(f"{tid}: using {mk}")
                break
        if not code:
            print(f"{tid}: no code anywhere"); continue
        xyz = os.path.join(OUT, f"{tid}.xyz")
        wrapper = PREAMBLE + "\n" + code + "\n" + EPILOGUE.replace("__OUT_XYZ__", repr(xyz))
        wf = os.path.join(SCRATCH, f"{tid}_neb.py")
        open(wf, "w").write(wrapper)
        r = subprocess.run(["conda", "run", "-n", "base", "python", wf],
                           capture_output=True, text=True, timeout=180, cwd=SCRATCH)
        tail = [l for l in (r.stdout + r.stderr).splitlines() if "NEB_" in l]
        print(f"{tid}: {tail[-1] if tail else (r.stderr.strip()[-80:] or '?')}")


if __name__ == "__main__":
    main()
