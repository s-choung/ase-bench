from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(f"Average coordination number: {np.mean(coord_numbers):.2f}")
