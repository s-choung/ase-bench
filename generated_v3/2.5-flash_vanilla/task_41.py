from ase import build
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import Trajectory, read
from ase import units

# Part 1: MD Simulation
# Create Cu FCC bulk
atoms = build.bulk('Cu', 'fcc', a=3.61, cubic=True)

# Attach EMT calculator
atoms.set_calculator(EMT())

# Set up MD parameters
temperature = 300  # Kelvin
timestep = 1.0     # fs
friction = 0.005   # 1/fs

# Initialize Langevin dynamics
dyn = Langevin(atoms, timestep * units.fs, temperature * units.kB, friction)

# Set up trajectory writer
traj_file = 'cu_md.traj'
traj = Trajectory(traj_file, 'w', atoms)
dyn.attach(traj.write, interval=1)

# Run MD for 10 steps
dyn.run(10)
traj.close()

# Part 2: Trajectory Analysis
# Read the trajectory file
frames = read(traj_file, index=':')

# Print total number of frames
print(f"Total number of frames in trajectory: {len(frames)}")

# Get the last frame and its potential energy
last_frame = frames[-1]
last_frame_energy = last_frame.get_potential_energy()
print(f"Potential energy of the last frame: {last_frame_energy:.3f} eV")
