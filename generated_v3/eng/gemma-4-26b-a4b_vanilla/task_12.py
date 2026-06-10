import numpy as np
from ase import Atoms
from ase.build import bulk

a = 2.95
c_over_a = 1.59
c = a * c_over_a

# HCP lattice vectors
lattice = [
    [a, 0, 0],
    [a * 0.5, a * np.sqrt(3) / 2, 0],
    [0, 0, c]
]

# Standard HCP basis positions (fractional)
basis = [
    [0, 0, 0],
    [2/3, 1/3, 1/2]
]

# Create structure
ti_hcp = Atoms('Ti2', 
               scaled_positions=basis, 
               cell=lattice, 
               pbc=True)

# Note: To make this a "bulk" crystal, we extend the unit cell
# Using ASE's built-in tiling logic to create a representative volume
ti_bulk = ti_hcp.repeat((4, 4, 3))

print("Cell Vectors:")
print(ti_bulk.get_cell())
print("\nAtomic Positions (first 10):")
print(ti_bulk.get_positions()[:10])
