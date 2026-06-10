from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create Cu FCC bulk and replicate to a 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms = atoms * (3, 3, 3)   # 3x3x3 supercell

# Determine cutoffs for each atom based on its element
cutoffs = natural_cutoffs(atoms)

# Build neighbor list (no self‑interaction, count both directions)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Number of neighbors for each atom
neighbor_counts = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

# Average coordination number
avg_coord = sum(neighbor_counts) / len(atoms)
print(f'Average coordination number: {avg_coord:.3f}')
