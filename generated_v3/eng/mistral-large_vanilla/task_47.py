from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

cu = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
cutoffs = natural_cutoffs(cu)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(cu)

coord_numbers = [nl.get_neighbors(i)[0].size for i in range(len(cu))]
avg_coord = sum(coord_numbers) / len(cu)
print(f"Average coordination number: {avg_coord:.2f}")
