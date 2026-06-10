from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Cu FCC 3×3×3 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Natural cut‑offs and neighbor list
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Coordination per atom
coord = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print('Average coordination number:', np.mean(coord))
