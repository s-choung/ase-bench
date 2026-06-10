from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read

# Build Cu FCC bulk & attach EMT
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize MD conditions
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD setup with trajectory saving
traj = Trajectory('md.traj', 'w')
md = VelocityVerlet(atoms, timestep=5*units.fs)
md.attach(traj.write, interval=1)
md.run(steps=10)
traj.close()

# Read trajectory and output results
frames = read('md.traj', index=':')
last_frame = frames[-1]
last_frame.calc = EMT()
print(f'Total frames: {len(frames)}')
print(f'Last frame energy: {last_frame.get_potential_energy()}')
