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
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Al", "fcc", a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

temperature = 500.0
pressure_gpa = 10.0
pressure_au = pressure_gpa / 160.21766208
bulk_modulus_al_gpa = 76.0
compressibility_au = 1.0 / (bulk_modulus_al_gpa / 160.21766208)

MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
Stationary(atoms)

print("Initial volume:", atoms.get_volume())

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=temperature,
    taut=100.0 * units.fs,
    pressure_au=pressure_au,
    taup=1000.0 * units.fs,
    compressibility_au=compressibility_au,
)

dyn.run(100)

print("Final volume:", atoms.get_volume())


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T31.xyz')
