from ase import Atoms
import numpy as np

# CO2: C at origin, O atoms at +/-1.16 A along x
d = 1.16
co2 = Atoms('COO', positions=[(0, 0, 0), (-d, 0, 0), (d, 0, 0)])
co2.set_cell([10, 10, 10])
co2.pbc = False

# Pairwise distances via get_distances
idx = np.arange(len(co2))
dist_matrix = co2.get_distances(idx, idx)

print("Pairwise distance matrix (Angstrom):")
print(dist_matrix)
print(f"\nC-O bond length: {co2.get_distance(0, 1):.3f} A")
print(f"O-O distance:   {co2.get_distance(1, 2):.3f} A")
