from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # Remove linear and angular momenta

# Print initial properties
print(f"Initial Temp: {atoms.get_temperature():.2f} K")
print(f"Initial Energy: {atoms.get_potential_energy():.6f} eV")

# Run Langevin MD
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(steps=100)

# Print final properties
print(f"Final Temp: {atoms.get_temperature():.2f} K")
print(f"Final Energy: {atoms.get_potential_energy():.6f} eV")
