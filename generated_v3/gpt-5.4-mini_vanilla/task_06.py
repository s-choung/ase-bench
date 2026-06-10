from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md import MDLogger
from ase.io import Trajectory
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

T = 300.0
dt = 5.0 * units.fs
steps = 100

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)
ZeroRotation(atoms)

def temp_and_energy(a):
    return a.get_temperature(), a.get_total_energy()

T0, E0 = temp_and_energy(atoms)
print(f"Initial: T = {T0:.2f} K, E = {E0:.6f} eV")

dyn = Langevin(atoms, dt, temperature_K=T, friction=0.01)

dyn.run(steps)

Tf, Ef = temp_and_energy(atoms)
print(f"Final:   T = {Tf:.2f} K, E = {Ef:.6f} eV")
