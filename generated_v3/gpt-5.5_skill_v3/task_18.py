from ase.build import molecule

atoms = molecule("CH4")

print("Chemical formula:", atoms.get_chemical_formula())

print("\nAtomic coordinates (Angstrom):")
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f"{i:2d} {atom.symbol:2s} {x:12.6f} {y:12.6f} {z:12.6f}")

c_index = [i for i, a in enumerate(atoms) if a.symbol == "C"][0]
h_indices = [i for i, a in enumerate(atoms) if a.symbol == "H"]

print("\nC-H bond lengths (Angstrom):")
for h in h_indices:
    d = atoms.get_distance(c_index, h)
    print(f"C{c_index}-H{h}: {d:.6f}")
