from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initialize velocities at 300 K and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Initial total energy
E_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Initial total energy: {E_init:.6f} eV')

# Run NVE MD for 50 steps
dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.run(50)

# Final total energy
E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Final total energy: {E_final:.6f} eV')
print(f'Energy change: {E_final - E_init:.6e} eV')
