from ase.build import molecule
import numpy as np

# Retrieve CH4 from G2 database
atoms = molecule('CH4')

# Print chemical formula
print("Chemical formula:", atoms.get_chemical_formula())

# Print atomic coordinates
print("\nAtomic coordinates (Å):")
for i, (symbol, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
    print(f"{i}: {symbol} {pos}")

# Calculate and print bond lengths
positions = atoms.get_positions()
c_pos = positions[0]  # Carbon atom

print("\nBond lengths (Å):")
for i in range(1, len(atoms)):  # Hydrogen atoms
    h_pos = positions[i]
    distance = np.linalg.norm(c_pos - h_pos)
    print(f"C-H{i}: {distance:.3f}")
