from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read, Trajectory
from ase import units

# Setup system
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD Simulation
traj = Trajectory('md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
dyn.attach(traj)
dyn.run(10)

# Analysis
frames = read('md.traj', index=':')
print(f"Total frames: {len(frames)}")
print(f"Last frame energy: {frames[-1].get_potential_energy():.4f} eV")
