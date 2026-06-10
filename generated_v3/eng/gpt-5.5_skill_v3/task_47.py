from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, skin=0.0, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])

print("Coordination numbers:", coord_numbers.tolist())
print(f"Average coordination number: {coord_numbers.mean():.2f}")
