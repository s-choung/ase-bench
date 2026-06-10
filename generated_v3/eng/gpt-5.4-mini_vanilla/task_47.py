from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coord_numbers.append(len(indices))

avg_coord = sum(coord_numbers) / len(coord_numbers)
print("Average coordination number:", avg_coord)
