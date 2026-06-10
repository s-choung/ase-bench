from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.io import write, read
import numpy as np

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Run MD for 10 steps
md = VelocityVerlet(atoms, timestep=1.0*units.fs)
trajectory = Trajectory('md.traj', 'w', atoms)
for i in range(10):
    md.run(1)
    trajectory.write(atoms)

# Read the trajectory back
atoms_read = read('md.traj', 'r', index=':')

# Print the number of frames and the energy of the last frame
print(f"Number of frames: {len(trajectory)}")
print(f"Energy of the last frame: {atoms_read.get_potential_energy()}")
