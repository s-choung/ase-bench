import numpy as np
from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = None

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

neighbor_counts = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    neighbor_counts.append(len(indices))

avg_coord = np.mean(neighbor_counts)
print(f"Average coordination number: {avg_coord:.2f}")
