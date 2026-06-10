import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

a_guess = 3.6
volumes, energies = [], []

for a in np.linspace(3.45, 3.75, 9):
    atoms = bulk("Cu", "fcc", a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()
a0 = v0 ** (1 / 3)

slab = fcc111("Cu", size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

slab.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in slab]))

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02, steps=300)

print(f"a0 = {a0:.6f} Ang")
print(f"Final energy = {slab.get_potential_energy():.8f} eV")

for tag in sorted(set(slab.get_tags())):
    zavg = slab.positions[slab.get_tags() == tag, 2].mean()
    print(f"Layer tag {tag}: z_avg = {zavg:.6f} Ang")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T49.xyz')
