import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (3, 3, 3)

nl = NeighborList(natural_cutoffs(atoms), self_interaction=False, bothways=True)
nl.update(atoms)

coordination_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

average_cn = np.mean(coordination_numbers)
print(f"Average coordination number: {average_cn:.2f}")
