from ase.build import molecule
from ase.data import atomic_numbers

# Retrieve CH4 from the G2 database
atoms = molecule('CH4')

# Print atomic coordinates
print("Atomic coordinates (Å):")
print(atoms.get_positions())

# Print bond lengths (C-H)
print("\nBond lengths (Å):")
for i in range(1, len(atoms)):
    dist = atoms.get_distance(0, i)
    print(f"C-H{i}: {dist:.4f}")

# Print chemical formula
print(f"\nChemical formula: {atoms.get_chemical_formula()}")
