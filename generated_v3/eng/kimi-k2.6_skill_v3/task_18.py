from ase.build import molecule

atoms = molecule('CH4')

print("Formula:", atoms.get_chemical_formula())

print("\nCoordinates (Å):")
for i, (sym, pos) in enumerate(zip(atoms.symbols, atoms.positions)):
    print(f"{i:2d} {sym:2s} {pos[0]:12.6f} {pos[1]:12.6f} {pos[2]:12.6f}")

c = next(i for i, s in enumerate(atoms.symbols) if s == 'C')
hs = [i for i, s in enumerate(atoms.symbols) if s == 'H']

print("\nBond lengths (Å):")
for h in hs:
    print(f"C—H({h}): {atoms.get_distance(c, h):.6f}")
