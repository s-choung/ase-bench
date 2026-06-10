from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import read, Trajectory

# Create Cu FCC bulk and attach EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Set up trajectory writer
traj = Trajectory('md.traj', 'w', atoms)

# Run short MD simulation (10 steps)
md = VelocityVerlet(atoms, timestep=1.0 * units.fs, trajectory=traj)
md.run(10)
traj.close()

# Read trajectory back
frames = read('md.traj', index=':')
if not isinstance(frames, list):
    frames = [frames]

# Print results
print(len(frames))
print(frames[-1].get_potential_energy())
