from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6) * (3,3,3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coord_numbers.append(len(indices))

print('Average coordination number: %.2f' % np.mean(coord_numbers))
