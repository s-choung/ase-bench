from ase import Atoms
from ase.build import hcp0001
import numpy as np

# Create HCP bulk structure manually to control a and c/a ratio
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# HCP unit cell: 2 atoms at (0,0,0) and (2/3,1/3,1/2)
positions = [[0, 0, 0],
             [2/3, 1/3, 1/2]]

# Build cell vectors for HCP
cell = [[a, 0, 0],
        [-a/2, a*np.sqrt(3)/2, 0],
        [0, 0, c]]

# Create atoms object
ti_bulk = Atoms('Ti2', positions=positions, cell=cell, pbc=True)

# Print cell vectors and atomic positions
print("Cell vectors (Å):")
print(ti_bulk.get_cell())
print("\nAtomic positions (fractional coordinates):")
print(ti_bulk.get_scaled_positions())
print("\nAtomic positions (cartesian coordinates, Å):")
print(ti_bulk.get_positions())
