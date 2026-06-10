from ase.collections import g2

atoms = g2['CH4']

print("Chemical Formula:", atoms.get_chemical_formula())

print("\nAtomic Coordinates (A):")
for symbol, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f"{symbol:2} {pos[0]:8.4f} {pos[1]:8.4f} {pos[2]:8.4f}")

print("\nBond Lengths (A):")
for i in range(1, len(atoms)):
    dist = atoms.get_distance(0, i)
    print(f"C-H (0-{i}): {dist:.4f}")
