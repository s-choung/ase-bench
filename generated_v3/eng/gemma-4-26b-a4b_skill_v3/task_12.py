import numpy as np
from ase import Atoms

# Constants
a = 2.95
c_over_a = 1.59
c = a * c_over_a

# Define HCP lattice vectors (hexagonal axes)
# a1 = (a, 0, 0)
# a2 = (-a/2, a*sqrt(3)/2, 0)
# a3 = (0, 0, c)
cell = [
    [a, 0, 0],
    [-a/2, a * np.sqrt(3)/2, 0],
    [0, 0, c]
]

# Define HCP basis positions (standard positions for space group P63/mmc)
# Atoms at (0,0,0) and (2/3, 1/3, 1/2) in fractional coordinates
basis = [
    [0, 0, 0],
    [2/3, 1/3, 1/2]
]

# Create Atoms object
ti_hcp = Atoms('Ti2', scaled_positions=basis, cell=cell, pbc=True)

# Output
print("Cell Vectors:")
print(ti_hcp.get_cell())
print("\nAtomic Positions (Cartesian):")
print(ti_hcp.get_positions())
