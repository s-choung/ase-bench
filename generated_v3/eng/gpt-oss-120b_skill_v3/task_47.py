from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Build 3×3×3 Cu fcc supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Coordination numbers
coords = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print("Average coordination number:", np.mean(coords))
