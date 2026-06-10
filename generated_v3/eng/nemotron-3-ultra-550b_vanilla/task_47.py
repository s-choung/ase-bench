from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList
import numpy as np

# Create Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)

# Build NeighborList with natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate coordination numbers
coordination = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])

# Print average coordination number
print(f"Average coordination number: {coordination.mean():.2f}")
