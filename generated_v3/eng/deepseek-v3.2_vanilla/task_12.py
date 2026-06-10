from ase import Atoms
import numpy as np

# Create Ti HCP bulk structure
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# HCP lattice vectors
cell = [[a, 0, 0],
        [-a/2, a*np.sqrt(3)/2,  

0],
        [0, 0, c]]

# Two atoms in HCP unit cell
positions = [[0, 0, 0],
             [a/2, a*np.sqrt(3)/6, c/2]]

ti = Atoms('Ti2', positions=positions, cell=cell, pbc=True)

print("Cell vectors (Å):")
print(ti.cell)
print("\nAtomic positions (Å):")
for i, pos in enumerate(ti.positions):
    print(f"Ti {i}: {pos}")
