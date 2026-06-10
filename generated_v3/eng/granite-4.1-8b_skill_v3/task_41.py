from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory, read
import numpy as np

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.615)

# Attach EMT calculator
atoms.calc = EMT()

# Perform MD with Langevin dynamics for 10 steps
md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
md_trajectory = Trajectory('cu_md.traj', 'w', atoms)

for step in range(10):
    md.run(1)  # single MD step
    md_trajectory.write(atoms)

# Close the trajectory file
md_trajectory.close()

# Read the trajectory back
traj = read('cu_md.traj')

# Print total number of frames and energy of the last frame
print(f"Total frames: {len(traj)}")
print(f"Energy of last frame: {traj[-1].get_potential_energy():.4f} eV")
