import numpy as np
from ase import Atoms
from ase.neighborlist import NeighborList, natural_cutoffs
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = None

cutoffs = natural_cutoffs(atoms, mult=1.2)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordination_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

avg_coord = np.mean(coordination_numbers)
print(f"Atoms: {len(atoms)}")
print(f"Average coordination number: {avg_coord:.2f}")
