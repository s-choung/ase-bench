from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True, skin=0.0)
nl.update(atoms)

coord_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_cn = np.mean(coord_numbers)

print(coord_numbers)
print(f"Average coordination number: {avg_cn:.2f}")
