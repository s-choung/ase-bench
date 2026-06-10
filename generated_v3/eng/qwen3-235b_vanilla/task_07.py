from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import VelocityVerlet
from ase import units

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Set EMT calculator
atoms.calc = EMT()

# Assign momenta corresponding to 300 K
MaxwellBoltzmannDistribution(atoms, 300 * units.kB)

# Print initial total energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {initial_energy:.3f} eV")

# Run NVE molecular dynamics
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
for _ in range(50):
    dyn.run(1)

# Print final total energy
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy: {final_energy:.3f} eV")
