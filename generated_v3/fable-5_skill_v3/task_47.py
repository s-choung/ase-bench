import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

counts = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(f"평균 coordination number: {np.mean(counts):.2f}")
