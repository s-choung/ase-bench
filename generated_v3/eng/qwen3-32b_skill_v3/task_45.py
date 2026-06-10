from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
import numpy as np

# Create H2 and calculate initial properties
h2 = molecule('H2')
initial_bond = h2.get_distance(0, 1)
h2.calc = EMT()
initial_energy = h2.get_potential_energy()

# Stretch to 0.9 Å and apply constraint
positions = np.array([[0, 0, 0], [0, 0, 0.9]])
h2.set_positions(positions)
h2.set_constraint(FixBondLength(0, 1))

# Calculate final properties
final_bond = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()

# Print results
print(f"Before:\nBond length = {initial_bond:.4f} Å, Energy = {initial_energy:.4f} eV")
print(f"After:\nBond length = {final_bond:.4f} Å, Energy = {final_energy:.4f} eV")
