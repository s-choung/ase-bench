from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Set initial temperature and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Initialize NVE MD
dyn = VelocityVerlet(atoms, 5 * units.fs)

# Initial energy
initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run MD
dyn.run(50)

# Final energy
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Print energies
print(f'Initial total energy: {initial_energy:.6f} eV')
print(f'Final total energy: {final_energy:.6f} eV')
