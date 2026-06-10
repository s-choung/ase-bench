from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, skin=0.0, self_interaction=False, bothways=True)
nl.update(atoms)

coordination = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])

print("Coordination numbers:", coordination.tolist())
print("Average coordination number:", coordination.mean())
