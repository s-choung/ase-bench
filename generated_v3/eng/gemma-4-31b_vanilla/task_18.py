from ase.build import molecule
from ase.build import g2

atoms = g2.CH4
print(f"Formula: {atoms.get_chemical_formula()}")
print("Coordinates:\n", atoms.get_positions())

# Calculate bond lengths between C (index 0) and H (indices 1-4)
dist = atoms.get_all_distances()
print("Bond lengths (C-H):")
for i in range(1, 5):
    print(f"Bond {0}-{i}: {dist[0, i]:.4f} Å")
