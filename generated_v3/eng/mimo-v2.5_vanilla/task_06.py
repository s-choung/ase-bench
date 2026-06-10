from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial velocities at 300K
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Print initial state
print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial energy: {atoms.get_total_energy():.2f} eV")

# Langevin dynamics at 300K
dyn = Langevin(atoms, 5 * units.fs, 300 * units.kB, 0.002)
dyn.run(100)

# Print final state
print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final energy: {atoms.get_total_energy():.2f} eV")
