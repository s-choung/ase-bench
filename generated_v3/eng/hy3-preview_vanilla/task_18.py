from ase.collections import g2

# Retrieve CH4 from G2 database
mol = g2['CH4']

# Print atomic coordinates
print("Atomic coordinates (Å):")
for atom in mol:
    print(f"{atom.symbol}: {atom.position}")

# Print bond lengths
print("\nBond lengths (Å):")
for i in range(len(mol)):
    for j in range(i + 1, len(mol)):
        dist = mol.get_distance(i, j)
        print(f"{mol[i].symbol}-{mol[j].symbol}: {dist:.3f}")

# Print chemical formula
print(f"\nChemical formula: {mol.get_chemical_formula()}")
