from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md import MDLogger
from ase.io import Trajectory
from ase.optimize import BFGS
from ase.md import MDLogger
from ase import Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import Langevin
from ase import units
from ase.md.velocitydistribution import Stationary, ZeroRotation
from ase.md import MDLogger
from ase.io import Trajectory
from ase.md import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

def temp_and_energy(a):
    return a.get_temperature(), a.get_potential_energy() + a.get_kinetic_energy()

t0, e0 = temp_and_energy(atoms)
print(f"Initial T = {t0:.2f} K, E = {e0:.6f} eV")

dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01)

dyn.run(100)

t1, e1 = temp_and_energy(atoms)
print(f"Final   T = {t1:.2f} K, E = {e1:.6f} eV")
