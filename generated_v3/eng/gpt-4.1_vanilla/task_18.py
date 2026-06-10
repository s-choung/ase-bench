from ase.collections import g2
from ase.geometry import get_distances

# Retrieve CH4 molecule from G2 database
ch4 = g2['CH4']

# Print atomic coordinates
print("Atomic coordinates (Å):")
for symbol, pos in zip(ch4.get_chemical_symbols(), ch4.positions):
    print(f"{symbol}: {pos}")

# Compute and print C-H bond lengths
print("\nC-H bond lengths (Å):")
c_index = ch4.get_chemical_symbols().index('C')
for i, symbol in enumerate(ch4.get_chemical_symbols()):
    if symbol == 'H':
        dist = ch4.get_distance(c_index, i)
        print(f"C-H: {dist:.4f}")

# Print chemical formula
print(f"\nChemical formula: {ch4.get_chemical_formula()}")
