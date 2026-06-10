from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create a 2x2x2 supercell of Cu FCC
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)

# Use EMT calculator
atoms.calc = EMT()

# Set up Langevin dynamics
dyn = Langevin(atoms, timestep=5 * units.fs, temperature=300 * units.K, friction=0.1)

# Record initial temperature and energy
initial_temp = atoms.get_temperature()
initial_energy = atoms.get_total_energy()

# Run MD for 100 steps
dyn.run(100)

# Record final temperature and energy
final_temp = atoms.get_temperature()
final_energy = atoms.get_total_energy()

# Print results
print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Final Temperature: {final_temp:.2f} K")
print(f"Final Energy: {final_energy:.4f} eV")
