from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Build 2x2x2 FCC Cu supercell and attach EMT calculator
atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up Langevin dynamics: 5 fs timestep, 300K bath, friction coefficient
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01)

# Print initial state
print(f"Initial -> E: {atoms.get_total_energy():.4f} eV, T: {atoms.get_temperature():.2f} K")

# Run MD for 100 steps
dyn.run(100)

# Print final state
print(f"Final   -> E: {atoms.get_total_energy():.4f} eV, T: {atoms.get_temperature():.2f} K")
