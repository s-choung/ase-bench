import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def pressure_bar(a):
    s = a.get_stress(voigt=False, include_ideal_gas=True)
    return -np.trace(s) / 3.0 / units.bar

print(f"Initial volume: {atoms.get_volume():.6f} A^3")
print(f"Initial pressure: {pressure_bar(atoms):.6f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=7.14e-7 / units.bar,
    logfile=None,
)

dyn.run(200)

print(f"Final volume: {atoms.get_volume():.6f} A^3")
print(f"Final pressure: {pressure_bar(atoms):.6f} bar")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T30.xyz')
