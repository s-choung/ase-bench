from ase.collections import g2

atoms = g2['CH4']

print(f"Chemical Formula: {atoms.get_chemical_formula()}")

print("\nAtomic Coordinates:")
for i, atom in enumerate(atoms):
    print(f"  Atom {i} ({atom.symbol}): {atom.position}")

print("\nBond Lengths:")
dists = atoms.get_all_distances()
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f"  {atoms[i].symbol}-{atoms[j].symbol} ({i}-{j}): {dists[i, j]:.4f} Å")
