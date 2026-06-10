from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coord_numbers.append(len(indices))

print(f"Total atoms: {len(atoms)}")
print(f"Coordination numbers: {coord_numbers}")
print(f"Average coordination number: {np.mean(coord_numbers):.4f}")
