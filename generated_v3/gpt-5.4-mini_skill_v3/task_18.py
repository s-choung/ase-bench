from ase.collections import g2
from ase.geometry import get_distances
import numpy as np

atoms = g2['CH4']

print("Chemical formula:", atoms.get_chemical_formula())
print("Atomic positions (Å):")
print(atoms.get_positions())

d = atoms.get_all_distances(mic=False)
pairs = []
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        pairs.append((i, j, d[i, j]))

print("Bond lengths (Å):")
for i, j, dist in pairs:
    print(f"{i}-{j}: {dist:.6f}")
