from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.velocitylimit import VelocityVerlet
from ase.md.md import MDLogger
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write
import numpy as np

# Create a 2x2x2 Pd FCC supercell
atoms = fcc111('Pd', size=(2, 2, 2), vacuum=10.0)

# Set the EMT calculator
atoms.calc = EMT()

# Initial temperature
T = 500  # Kelvin
dt = 2.0  # fs
nsteps = 200

# Set initial velocities
atoms.set_velocities(atoms.get_temperature(scaled_units=True) * T)

# Get initial total energy
initial_energy = atoms.get_total_energy()

# Run NVE MD simulation
dyn = VelocityVerlet(atoms, dt)
dyn.run(nsteps)

# Get final total energy
final_energy = atoms.get_total_energy()

# Print energy difference
print(f"Initial total energy: {initial_energy:.4f} eV")
print(f"Final total energy: {final_energy:.4f} eV")
print(f"Energy difference: {final_energy - initial_energy:.4f} eV")
