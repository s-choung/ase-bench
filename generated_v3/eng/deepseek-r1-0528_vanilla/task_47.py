from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
cutoffs = natural_cutoffs(atoms, mult=1.2)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True, skin=0.0)
nl.update(atoms)
coords = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(np.mean(coords))
