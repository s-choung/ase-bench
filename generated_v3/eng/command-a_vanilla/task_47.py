from ase import Atoms
from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList
import numpy as np

# Create Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
cu = cu.repeat((3, 3, 3))

# Define natural cutoffs
cutoffs = natural_cutoffs(cu)

# Build NeighborList
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(cu)

# Calculate number of neighbors for each atom
num_neighbors = np.array([len(neighbors) for atom, neighbors in nl.get_neighbors()])

# Print average coordination number
print(f'Average coordination number: {np.mean(num_neighbors):.2f}')
