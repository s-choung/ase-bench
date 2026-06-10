from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.9) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocity from 500 K, remove drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Get initial total energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run NVE MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Get final total energy
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Print energy difference
print(f"Energy change: {final_energy - initial_energy:.6f} eV")
