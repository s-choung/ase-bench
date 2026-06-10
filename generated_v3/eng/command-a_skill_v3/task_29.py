from ase import units
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial temperature to 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Remove COM motion

# Initial total energy
initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run NVE MD
dyn = VelocityVerlet(atoms, timestep=2*units.fs)
dyn.run(200)

# Final total energy
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Print energy difference
print(f"Energy difference: {final_energy - initial_energy:.6f} eV")
