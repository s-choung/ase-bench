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
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial T = {atoms.get_temperature():.2f} K")
print(f"Initial Epot = {atoms.get_potential_energy():.6f} eV")
print(f"Initial Etot = {atoms.get_total_energy():.6f} eV")

dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)
dyn.run(100)

print(f"Final T = {atoms.get_temperature():.2f} K")
print(f"Final Epot = {atoms.get_potential_energy():.6f} eV")
print(f"Final Etot = {atoms.get_total_energy():.6f} eV")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T06.xyz')
