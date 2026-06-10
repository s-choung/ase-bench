from ase.collections import g2
from ase.neighborlist import neighbor_list
import numpy as np

atoms = g2['CH4']

print('Coordinates (Å):')
print(atoms.get_positions())

print('Formula:', atoms.get_chemical_formula())

cutoff = 1.2  # Å, suitable for C–H bonds
i, j = neighbor_list('ij', atoms, cutoff=cutoff)
distances = np.linalg.norm(atoms.positions[i] - atoms.positions[j], axis=1)

print('Bond lengths (Å):')
for d in distances:
    print(f'{d:.3f}')
