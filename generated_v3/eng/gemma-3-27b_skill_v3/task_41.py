from ase import Atoms
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.io import Trajectory
from ase.calculators.emt import EMT
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

traj = Trajectory('cu_md.traj', 'w', atoms)

md = VelocityVerlet(atoms, timestep=0.001)  # Example timestep
for i in range(10):
    md.run(1)
    traj.write(atoms)

del md
del traj

trajectory = Trajectory('cu_md.traj', 'r')
num_frames = len(trajectory)
print(f"Number of frames in trajectory: {num_frames}")

trajectory.get_atoms().calc = EMT()
last_frame_energy = trajectory.get_atoms().get_potential_energy()
print(f"Energy of the last frame: {last_frame_energy} eV")

trajectory.close()
