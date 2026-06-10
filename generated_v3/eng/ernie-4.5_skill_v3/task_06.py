from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import (
    MaxwellBoltzmannDistribution,
    Stationary,
)

# Create Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial velocities (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # Remove COM motion

# Print initial state
print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

# Run Langevin MD
md = Langevin(atoms, 
              timestep=5 * units.fs,
              temperature_K=300,
              friction=0.01 / units.fs)
md.run(100)

# Print final state
print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
