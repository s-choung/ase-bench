from ase import Atoms
import numpy as np

# HCP unit cell parameters
a = 2.95  # angstrom
c = 1.59 * a  # c/a ratio = 1.59

# HCP cell vectors
cell = [[a, 0, 0],
        [-a/2, a*np.sqrt(3)/2, 0],
        [0, 0, c]]

# Atomic positions (fractional coordinates)
positions = [[0, 0, 0],
             [2/3, 1/3, 0.5]]

# Create Ti HCP structure
ti_hcp = Atoms('Ti2', positions=positions, cell=cell, pbc=True)

# Print cell vectors
print("Cell vectors (ang):")
print(np.array(cell))

# Print atomic positions in Cartesian coordinates
print("\nAtomic positions (ang):")
print(ti_hcp.get_positions())
