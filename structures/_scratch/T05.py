import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms0 = bulk("Cu", "fcc", a=3.6, cubic=True)

volumes = []
energies = []

for s in np.linspace(0.94, 1.06, 13):
    atoms = atoms0.copy()
    atoms.set_cell(atoms0.cell * s, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos="birchmurnaghan")
v0, e0, B = eos.fit()

a0 = v0 ** (1.0 / 3.0)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant a0 = {a0:.6f} Å")
print(f"Equilibrium volume V0 = {v0:.6f} Å^3")
print(f"Bulk modulus B = {B_GPa:.6f} GPa")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T05.xyz')
