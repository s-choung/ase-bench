from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.md import MDLogger
from ase.io import vasp
from ase.units import fs
import numpy as np

# Define the Cu FCC bulk with a 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))

# Assign the EMT calculator
atoms.calc = EMT()

# Set initial velocities using Maxwell-Boltzmann distribution at T=300K
MaxwellBoltzmannDistribution(atoms, 300 * fs)

# Set up the Langevin dynamics
dyn = Langevin(atoms, 5 * fs, 0.1, 300 * fs)

# Attach the MDLogger to print initial energy and temperature
MDLogger(atoms, 'md.log', header=False).start()

# Get initial temperature and potential energy
initial_temp = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()
print(f'Initial Temperature: {initial_temp:.2f} K')
print(f'Initial Potential Energy: {initial_energy:.2f} eV')

# Run the MD simulation
dyn.run(100)

# Get the final temperature and potential energy
final_temp = atoms.get_temperature()
final_energy = atoms.get_potential_energy()
print(f'Final Temperature: {final_temp:.2f} K')
print(f'Final Potential Energy: {final_energy:.2f} eV')
