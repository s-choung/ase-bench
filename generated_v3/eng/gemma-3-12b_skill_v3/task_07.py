from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dt = 5 * units.fs
md = VelocityVerlet(atoms, dt)

initial_energy = atoms.get_potential_energy() + np.sum([a.get_kinetic_energy() for a in atoms])

md.run(50)

final_energy = atoms.get_potential_energy() + np.sum([a.get_kinetic_energy() for a in atoms])

print(f"Initial total energy: {initial_energy}")
print(f"Final total energy: {final_energy}")
