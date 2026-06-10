from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase import units

# Setup system
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initial relaxation
BFGS(atoms).run(fmax=0.05)

# MD Preparation
print(f"Initial Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Initial Temperature: {atoms.get_temperature():.2f} K")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin MD
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
dyn.run(100)

# Output results
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final Temperature: {atoms.get_temperature():.2f} K")
