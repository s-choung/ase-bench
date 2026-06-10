from ase.build import molecule

ch4 = molecule('CH4')

print("Atomic coordinates (Å):")
print(ch4.positions)

print("\nChemical formula:", ch4.get_chemical_formula())

print("\nBond lengths (C-H):")
c_idx = next(i for i, s in enumerate(ch4.get_chemical_symbols()) if s == 'C')
for i, s in enumerate(ch4.get_chemical_symbols()):
    if s == 'H':
        dist = ch4.get_distance(c_idx, i)
        print(f"H{i}: {dist:.3f} Å")
