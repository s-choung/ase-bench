from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase import units

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Run MD and save trajectory
traj_file = 'md.traj'
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
traj = Trajectory(traj_file, 'w', atoms)
dyn.attach(traj.write, interval=1)
dyn.run(steps=10)
traj.close()

# Read trajectory back
traj_read = Trajectory(traj_file, 'r')
frames = list(traj_read)
n_frames = len(frames)
last_energy = frames[-1].get_potential_energy()
print(f'Number of frames: {n_frames}')
print(f'Energy of last frame: {last_energy:.6f} eV')
