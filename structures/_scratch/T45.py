import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms("H2", positions=[(0, 0, 0), (0, 0, 0.74)])
h2.calc = EMT()

print("Before constraint:")
print("bond length =", h2.get_distance(0, 1), "Ang")
print("energy =", h2.get_potential_energy(), "eV")

h2.set_distance(0, 1, 0.9, fix=0)
h2.set_constraint(FixBondLength(0, 1))

print("After constraint:")
print("bond length =", h2.get_distance(0, 1), "Ang")
print("energy =", h2.get_potential_energy(), "eV")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T45.xyz')
