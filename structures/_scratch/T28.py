import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T0, T1 = 300.0, 600.0
steps = 200
dt = 5 * units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)

dyn = Langevin(
    atoms,
    timestep=dt,
    temperature_K=T0,
    friction=0.01 / units.fs,
)

for step in range(1, steps + 1):
    target_T = T0 + (T1 - T0) * (step - 1) / (steps - 1)
    dyn.set_temperature(temperature_K=target_T)
    dyn.run(1)

    if step % 50 == 0:
        print(f"Step {step}: T = {atoms.get_temperature():.2f} K")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T28.xyz')
