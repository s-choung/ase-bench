from ase.build import molecule

# Get CH4 molecule from G2 database
atoms = molecule('CH4')

# Print atomic coordinates
print("Atomic coordinates (Å):")
print(atoms.get_positions())

# Print chemical formula
print("\nChemical formula:", atoms.get_chemical_formula())

# Print bond lengths
print("\nBond lengths (Å):")
for i in range(len(atoms)):
    for j in range(i+1, len(atoms)):
        dist = atoms.get_distance(i, j)
        print(f"{atoms[i].symbol}-{atoms[j].symbol}: {dist:.3f}")
