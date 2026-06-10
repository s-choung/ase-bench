from ase.build import molecule

atoms = molecule('CH4')

print("Chemical formula:", atoms.get_chemical_formula())

print("\nAtomic positions:")
for atom in atoms:
    print(f"{atom.symbol}: {atom.position}")

print("\nBond lengths (C-H):")
for i in range(1, len(atoms)):
    d = atoms.get_distance(0, i)
    print(f"{atoms[0].symbol}-{atoms[i].symbol} ({0}-{i}): {d:.4f} Å")
