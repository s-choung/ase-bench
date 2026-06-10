from ase.collections.g2 import g2

atoms = g2['CH4']

print("Atomic coordinates (Å):")
for atom in atoms:
    print(f"{atom.symbol} {atom.x:.6f} {atom.y:.6f} {atom.z:.6f}")

c_idx = [i for i, a in enumerate(atoms) if a.symbol == 'C'][0]
h_indices = [i for i, a in enumerate(atoms) if a.symbol == 'H']

print("\nBond lengths (Å):")
for i, h in enumerate(h_indices, 1):
    d = atoms.get_distance(c_idx, h)
    print(f"C-H{i}: {d:.6f}")

print("\nChemical formula:", atoms.get_chemical_formula())
