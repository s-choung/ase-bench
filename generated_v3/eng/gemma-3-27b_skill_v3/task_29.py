from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs
import numpy as np

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

md = VelocityVerlet(atoms, timestep=2 * fs)
md.run(200)

final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

energy_difference = final_energy - initial_energy
print(f"Energy difference: {energy_difference:.5f} eV")
