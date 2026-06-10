from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Setup structure and calculator
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial state
print(f"Initial Temp: {atoms.get_temperature():.2f} K")
print(f"Initial Energy: {atoms.get_total_energy():.4f} eV")

# Run Langevin MD
md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
md.run(100)

# Print final state
print(f"Final Temp: {atoms.get_temperature():.2f} K")
print(f"Final Energy: {atoms.get_total_energy():.4f} eV")
