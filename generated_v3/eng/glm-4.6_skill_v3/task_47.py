import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs=cutoffs, skin=0.2, bothways=True, self_interaction=False)
nl.update(atoms)

neighbor_counts = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

avg_coordination = np.mean(neighbor_counts)
print(f"Average coordination number: {avg_coordination:.2f}")
