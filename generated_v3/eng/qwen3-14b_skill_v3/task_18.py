from ase.collections.g2 import g2
from ase.geometry import get_distances

for atoms in g2:
    if atoms.get_chemical_formula() == 'CH4':
        break

print(f"Chemical Formula: {atoms.get_chemical_formula()}\n")
print("Coordinates (Å):")
for i, (s, p) in enumerate(zip(atoms.symbols, atoms.positions), 1):
    print(f"{i}. {s}: {p}")

print("\nBond Lengths (Å):")
dist = get_distances(atoms, [0], list(range(1,5)))
for i, d in enumerate(dist[0], 1):
    print(f"C-H {i}: {d:.3f}")
