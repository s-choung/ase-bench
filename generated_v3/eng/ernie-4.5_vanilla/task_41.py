from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.io.trajectory import Trajectory

# Create FCC Cu bulk
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)

# Attach EMT calculator
atoms.calc = EMT()

# Set momentum to zero
atoms.set_momentum(0)

# Apply thermal velocity
MaxwellBoltzmannDistribution(atoms, 300)

# Create MD object with timestep in fs
md = VelocityVerlet(atoms, 5 * 0.001)  # 5 fs timestep

# Create a trajectory object
traj = Trajectory('md_trajectory.traj', 'w', atoms)

# Run MD for 10 steps and save to trajectory
for _ in range(10):
    md.run(1)
    traj.write(atoms)

# Read trajectory back
traj = Trajectory('md_trajectory.traj', 'r')

# Print number of frames
print(f"Number of frames: {len(traj)}")

# Print energy of the last frame
last_frame = traj[-1]
print(f"Energy of last frame: {last_frame.get_potential_energy():.2f} eV")
