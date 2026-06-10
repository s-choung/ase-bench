from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities to 300K Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Print initial state
print(f"Initial: Temperature = {atoms.get_temperature():.1f} K, Total Energy = {atoms.get_total_energy():.3f} eV")

# Set up Langevin dynamics
dyn = Langevin(
    atoms,
    timestep=5*units.fs,
    temperature_K=300,
    friction=0.01/units.fs
)

# Run 100 MD steps
dyn.run(100)

# Print final state
print(f"Final:   Temperature = {atoms.get_temperature():.1f} K, Total Energy = {atoms.get_total_energy():.3f} eV")
