import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (3, 3, 3)

# Get natural cutoffs based on atomic species
cutoffs, offsets = natural_cutoffs(atoms)

# Build NeighborList
nl = NeighborList(cutoffs, offsets, atoms, skin=2.0)
nl.update(atoms)

# Calculate coordination numbers
n_neighbors = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    n_neighbors.append(len(indices))

# Output results
avg_cn = np.mean(n_neighbors)
print(f"Coordination numbers per atom: {n_neighbors}")
print(f"Average coordination number: {avg_cn:.2f}")
