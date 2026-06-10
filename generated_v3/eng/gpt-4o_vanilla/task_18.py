from ase.build import molecule
from ase.data.g2 import molecule as g2_molecule

# Retrieve CH4 from the ASE G2 database
ch4 = g2_molecule('CH4')

# Print atomic coordinates
print("Atomic Coordinates:")
for atom in ch4:
    print(f"{atom.symbol}: {atom.position}")

# Calculate and print bond lengths
bond_lengths = [ch4.get_distance(i, j) for i in range(len(ch4)) for j in range(i+1, len(ch4))]
print("\nBond Lengths:")
for length in bond_lengths:
    print(length)

# Print chemical formula
print("\nChemical Formula:")
print(ch4.get_chemical_formula())
