import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111("Cu", size=(2, 2, 4), a=3.615, vacuum=10.0)

mask = [atom.tag >= 3 for atom in slab]
fixed_indices = np.where(mask)[0]
pos_before = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

opt = BFGS(slab, logfile="-")
opt.run(fmax=0.05, steps=200)

pos_after = slab.positions[fixed_indices].copy()
disp = np.linalg.norm(pos_after - pos_before, axis=1)

print("fixed_indices:", fixed_indices.tolist())
print("fixed_tags:", [slab[i].tag for i in fixed_indices])
print("positions_before:\n", pos_before)
print("positions_after:\n", pos_after)
print("displacements_A:", disp)
print("max_displacement_A:", disp.max())
print("fixed_atoms_unchanged:", np.allclose(pos_before, pos_after, atol=1e-12))


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T44.xyz')
