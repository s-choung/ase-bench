from ase.build import bulk
import numpy as np

# Cu fcc bulk, 2 × 2 × 2 supercell
atoms = bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))

# distances from atom 0 to every atom (including itself)
dist_all = atoms.get_distances(0, mic=True)

# discard the zero distance to itself
distances = dist_all[1:]

print(f"Number of atoms: {len(atoms)}")
print(f"Min distance (Å): {distances.min():.4f}")
print(f"Max distance (Å): {distances.max():.4f}")
