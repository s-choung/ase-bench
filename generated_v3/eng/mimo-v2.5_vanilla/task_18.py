from ase.io.g2 import get_g2_molecule
from ase import Atoms
import numpy as np

# Retrieve CH4 from G2 database
ch4 = get_g2_molecule('CH4')

# Print chemical formula
print("Chemical formula:", ch4.get_chemical_formula())

# Print atomic coordinates
print("\nAtomic coordinates (in Å):")
print(ch4.get_positions())

# Calculate and print bond lengths
carbon_idx = 0  # Carbon is first atom in CH4
hydrogen_indices = [1, 2, 3, 4]  # Hydrogen atoms

print("\nC-H bond lengths (in Å):")
for h_idx in hydrogen_indices:
    distance = ch4.get_distance(carbon_idx, h_idx)
    print(f"C-H{h_idx}: {distance:.3f}")
