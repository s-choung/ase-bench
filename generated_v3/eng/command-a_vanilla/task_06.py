from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import kB

# Create Cu FCC bulk 2x2x2 supercell
cu = Atoms('Cu4', cell=[[4, 0, 0], [0, 4, 0], [0, 0, 4]], pbc=True)
cu.center()

# Attach EMT calculator
cu.calc = EMT()

# Initialize Langevin dynamics
dyn = Langevin(cu, timestep=5 * 1e-3, temperature_K=300, friction=0.01)

# Print initial properties
print(f"Initial temperature: {cu.get_temperature():.2f} K")
print(f"Initial energy: {cu.get_potential_energy():.4f} eV")

# Run MD for 100 steps
dyn.run(100)

# Print final properties
print(f"Final temperature: {cu.get_temperature():.2f} K")
print(f"Final energy: {cu.get_potential_energy():.4f} eV")
