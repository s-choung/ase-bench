from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory
from ase.io import read

# Build Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Attach EMT calculator
atoms.calc = EMT()

# Initialize velocities at 300K and remove drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Run MD for 10 steps, saving to trajectory
traj = Trajectory('cu_md.traj', 'w', atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs, trajectory=traj)
dyn.run(steps=10)

# Read trajectory back and analyze
traj_read = read('cu_md.traj', index=':')
print(f'Number of frames: {len(traj_read)}')
last_atoms = traj_read[-1]
last_atoms.calc = EMT()
print(f'Last frame energy: {last_atoms.get_potential_energy():.6f} eV')
