from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# FCC Cu 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)

# Build neighbor list with natural (covalent) cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors for each atom and compute average
neighbor_counts = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coordination = sum(neighbor_counts) / len(atoms)

print(f"Average coordination number: {avg_coordination:.1f}")
