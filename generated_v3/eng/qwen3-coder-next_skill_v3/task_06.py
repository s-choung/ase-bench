from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.langevin import Langevin
from ase import units

# Create 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (2, 2, 2)
atoms.calc = EMT()

# Set initial temperature and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial properties
T0 = atoms.get_temperature()
E0 = atoms.get_potential_energy()
print(f'Initial: T = {T0:.1f} K, E = {E0:.6f} eV')

# Run Langevin MD
langevin = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
langevin.run(100)

# Print final properties
T1 = atoms.get_temperature()
E1 = atoms.get_potential_energy()
print(f'Final:   T = {T1:.1f} K, E = {E1:.6f} eV')
