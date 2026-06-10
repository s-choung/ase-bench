from ase import units
from ase.build import bulk
from ase.md import VelocityVerlet
from ase.io import Trajectory
from ase.calculators.emt import EMT

# Define parameters for molecular dynamics
n_steps = 10
dt = 1 * units.fs

# Initialize Cu FCC bulk using the EMT calculator
cu_fcc = bulk('Cu', 'fcc', 3)
cu_fcc.center()
cu_fcc.calc = EMT()

# Define the MD trajectory
trajectory = Trajectory('md.traj', 'w', Cu(fcc))

# Set up the MD driver
md = VelocityVerlet(cu_fcc, dt)
md.attach(trajectory)

# Run molecular dynamics
md.run(n_steps)

# Read the trajectory file back
traj = Trajectory('md.traj')
frames = traj.read()

# Print the number of frames and the energy of the last frame
print(f"Total number of frames: {len(frames)}")
print(f"Energy of the last frame: {frames[-1].get_potential_energy().real} eV")
