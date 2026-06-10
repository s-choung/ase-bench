from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read, write

# Create Cu FCC bulk
atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[[0, 1.81, 1.81], [1.81, 0, 1.81], [1.81, 1.81, 0]], pbc=True)
atoms *= (2, 2, Kuz2)

# Attach EMT calculator
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Run MD
dyn = VelocityVerlet(atoms, timestep=5*units.fs, trajectory='md.traj')
dyn.run(10)

# Read trajectory
traj = read('md.traj', index=':')
print(f'Total frames: {len(traj)}')
last_atoms = traj[-1]
last_atoms.calc = EMT()
print(f'Last frame energy: {last_atoms.get_potential_energy():.3f} eV')
