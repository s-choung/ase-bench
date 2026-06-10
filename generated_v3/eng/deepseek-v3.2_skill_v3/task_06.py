from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import numpy as np

# Create 2x2x2 supercell of Cu FCC
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Initialize MD
md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, 
              friction=0.01 / units.fs)

# Print initial state
print(f"Initial T: {atoms.get_temperature():.2f} K")
print(f"Initial E: {atoms.get_potential_energy():.6f} eV")

# Run MD
md.run(steps=100)

# Print final state
print(f"Final T: {atoms.get_temperature():.2f} K")
print(f"Final E: {atoms.get_potential_energy():.6f} eV")
