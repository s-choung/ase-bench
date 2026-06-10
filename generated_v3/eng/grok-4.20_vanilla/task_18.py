from ase.build import molecule
from ase.geometry import get_distances
import numpy as np

# Retrieve CH4 from G2 database
atoms = molecule('CH4')

print('Chemical formula:', atoms.get_chemical_formula())
print('\nAtomic coordinates (Å):')
for sym, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f'{sym:2} {pos[0]:10.6f} {pos[1]:10.6f} {pos[2]:10.6f}')

# Calculate C-H bond lengths
pos = atoms.get_positions()
c_pos = pos[0]
h_pos = pos[1:]
dists = np.linalg.norm(h_pos - c_pos, axis=1)

print('\nC-H bond lengths (Å):')
for i, d in enumerate(dists, 1):
    print(f'{i}: {d:.6f}')
