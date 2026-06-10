from ase.build import molecule
from ase.geometry import get_distances

atoms = molecule('CH4')

print("Chemical Formula:", atoms.get_chemical_formula())
print("\nAtomic Positions (Å):")
for i, atom in enumerate(atoms):
    print(f"  {i}: {atom.symbol:2s} {atom.position}")

distances, d_indices = get_distances(atoms, mic=False)
print("\nBond Lengths (Å):")
for i in range(len(atoms)):
    for j in range(i+1, len(atoms)):
        idx = i * len(atoms) + j - (i+1) * (i+2) // 2
        if idx < len(distances):
            d = distances[idx]
            if d < 2.0:
                print(f"  {i}-{j}: {d:.4f}")
