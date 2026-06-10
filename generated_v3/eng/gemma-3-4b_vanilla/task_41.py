from ase import Atoms
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.io importTrajectory
import numpy as np

# Create Cu FCC bulk
atoms = Atoms.from_miller_indices([(1,0,0), (0,1,0), (0,0,1)], LatticeVectors.cubic(2.54), LatticeParam = 3.615)

# Set up EMT calculator
calc = EMT()
atoms.set_calculator(calc)

# Run MD for 10 steps
md = VelocityVerlet(atoms, box_type='cubic')
md.attach(10)

# Save trajectory
traj = Trajectory('cu_trajectory.traj')
traj.write(atoms)

# Read trajectory
atoms = Atoms.read_traj('cu_trajectory.traj')

# Print total number of frames and energy of the last frame
num_frames = len(atoms)
last_frame_energy = atoms[-1].get_potential_energy()

print(f"Total number of frames: {num_frames}")
print(f"Energy of the last frame: {last_frame_energy}")
