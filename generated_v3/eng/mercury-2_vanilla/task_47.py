from ase import Atoms
from ase.build import bulk, make_supercell
from ase.neighborlist import natural_cutoffs, NeighborList
import numpy as np

# Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.6)          # lattice constant ~3.6 Å
cell = np.eye(3) * 3                 # 3x3x3 replication
atoms = make_supercell(cu, cell)

# Natural cutoffs and neighbor list
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors per atom
nbr_counts = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])

# Average coordination number
avg_coord = nbr_counts.mean()
print(f'Average coordination number: {avg_coord:.2f}')
