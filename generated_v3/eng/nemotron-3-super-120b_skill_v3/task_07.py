from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms.calc = EMT()

# Initial velocities (300 K) and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Initial total energy
E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Initial total energy: {E0:.4f} eV')

# NVE MD with VelocityVerlet
dt = 5 * units.fs
dyn = VelocityVerlet(atoms, dt)
dyn.run(50)

# Final total energy
E1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Final total energy: {E1:.4f} eV')
print(f'Energy drift: {E1 - E0:.4e} eV')
