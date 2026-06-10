from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)

# Set calculator
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial state
print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial potential energy: {atoms.get_potential_energy():.3f} eV")
print(f"Initial kinetic energy: {atoms.get_kinetic_energy():.3f} eV")

# Run Langevin NVT MD
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.run(100)

# Print final state
print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final potential energy: {atoms.get_potential_energy():.3f} eV")
print(f"Final kinetic energy: {atoms.get_kinetic_energy():.3f} eV")
