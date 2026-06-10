import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase.build import molecule

atoms = molecule("CH4")

print("Chemical formula:", atoms.get_chemical_formula())

print("\nAtomic coordinates (Angstrom):")
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f"{i:2d} {atom.symbol:2s} {x:12.6f} {y:12.6f} {z:12.6f}")

c_index = [i for i, a in enumerate(atoms) if a.symbol == "C"][0]
h_indices = [i for i, a in enumerate(atoms) if a.symbol == "H"]

print("\nC-H bond lengths (Angstrom):")
for h in h_indices:
    d = atoms.get_distance(c_index, h)
    print(f"C{c_index}-H{h}: {d:.6f}")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T18.xyz')
