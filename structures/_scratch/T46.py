import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111("Pt", size=(2, 2, 3), vacuum=10.0)
co = Atoms("CO", positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.15]])

add_adsorbate(slab, co, height=1.8, position="ontop")

c_idx = len(slab) - 2
o_idx = len(slab) - 1

fix_bottom = FixAtoms(mask=[atom.tag == 3 for atom in slab])
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_co])

slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

print("Final energy (eV):", slab.get_potential_energy())
print("C-O distance (A):", slab.get_distance(c_idx, o_idx))


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T46.xyz')
