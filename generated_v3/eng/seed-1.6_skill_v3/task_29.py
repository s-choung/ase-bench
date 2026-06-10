from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Set up NVE MD
md = VelocityVerlet(atoms, timestep=2 * units.fs)

# Calculate initial total energy
initial_total = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run MD
md.run(steps=200)

# Calculate final total energy and print difference
final_total = atoms.get_total_energy() + atoms.get_kinetic_energy()
print(f"Energy difference (end - start): {final_total - initial_total:.6f} eV")
