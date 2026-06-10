import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.units import fs, kB, bar, kJ, Bohr, Hartree
from ase.positions import Trajectory
from ase.visualize import view

# Create a Pd FCC 2x2x2 supercell
a = 3.82  # Angstrom
atoms = bulk('Pd', 'fcc', a=a, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# Set the EMT calculator
atoms.calc = EMT()

# Set the MD parameters
timestep = 2 * fs
temperature = 500 * kB
friction = 0.01 * kB / fs

# Set up the MD simulation
md = VelocityVerlet(atoms, timestep=timestep)

# Run the MD simulation for 200 steps
num_steps = 200
md.run(num_steps)

# Print the total energy difference between the start and end of the simulation
initial_energy = atoms.get_potential_energy()
final_energy = atoms.get_potential_energy()
energy_difference = final_energy - initial_energy

print(f"Initial Energy: {initial_energy}")
print(f"Final Energy: {final_energy}")
print(f"Energy Difference: {energy_difference}")

# Optionally visualize the final structure
#view(atoms)
#Trajectory('md.traj', 'w', atoms)
