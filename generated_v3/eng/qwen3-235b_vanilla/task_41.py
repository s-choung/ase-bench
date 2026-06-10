from ase import Atoms, Atom
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase import units
from ase.io import Trajectory, read

# Create Cu FCC bulk structure
cu = bulk('Cu', 'fcc', a=3.6)

# Attach EMT calculator
cu.calc = EMT()

# Set initial velocities for MD
cu.set_temperature(300)

# Create trajectory file and MD object
traj_file = 'cu_md.traj'
traj = Trajectory(traj_file, 'w', cu)
md = VelocityVerlet(cu, timestep=1 * units.fs, trajectory=traj)

# Run MD for 10 steps
for _ in range(10):
    md.run(1)

# Close trajectory
traj.close()

# Read trajectory back
frames = read(traj_file, ':')
print(len(frames))
print(frames[-1].get_potential_energy())
