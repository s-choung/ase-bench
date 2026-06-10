from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Create a 3x3x3 supercell of Cu
a = 3.6  # Cu lattice constant
atoms = bulk('Cu', 'fcc', a=a, cubic=True, orthorhombic=True).repeat((3, 3, 3))

# Create a NeighborList
nl = NeighborList(atoms)
nl.build(cutoff=4.0*a)  # Natural cutoff
nl.compute_features()

# Get the number of neighbors for each atom
num_neighbors = np.array([nl.get_num_neighbors(i) for i in range(len(atoms))])

# Calculate the average coordination number
avg_coord_num = np.mean(num_neighbors)

print(f"Average coordination number: {avg_coord_num}")
