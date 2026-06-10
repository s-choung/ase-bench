from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, kB, bar, kJ, Bohr, Hartree
import numpy as np

# Create a Cu FCC bulk supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True, gamma=1)
atoms.set_cell([3.6, 3.6, 3.6])  # Explicitly set cell for better control
atoms.calc = EMT()

# Set up Langevin MD
temperature = 300.0
friction = 0.01 / fs
timestep = 5 * fs

langevin = Langevin(atoms, timestep=timestep, temperature_K=temperature, friction=friction)

# Run MD for 300 steps
for i in range(300):
    langevin.run()

# Print initial and final temperature and energy
initial_temperature = atoms.get_temperature()
final_temperature = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()
final_energy = atoms.get_potential_energy()

print(f"Initial Temperature: {initial_temperature:.2f} K")
print(f"Final Temperature: {final_temperature:.2f} K")
print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Final Energy: {final_energy:.4f} eV")
