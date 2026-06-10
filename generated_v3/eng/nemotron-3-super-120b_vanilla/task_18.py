from ase.db import G2

# Retrieve CH4 from the G2 database
g2 = G2()
atoms = g2.get_atoms(formula='CH4')

# Atomic coordinates
print("Atomic coordinates (Å):")
print(atoms.get_positions())

# C-H bond lengths
c_index = next(i for i, a in enumerate(atoms) if a.symbol == 'C')
print("\nBond lengths (C-H):")
for i, a in enumerate(atoms):
    if a.symbol == 'H':
        d = atoms.get_distance(c_index, i, mic=False)
        print(f"H{i}: {d:.3f} Å")

# Chemical formula
print("\nChemical formula:", atoms.get_chemical_formula())
