from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coord = sum(coord_numbers) / len(coord_numbers)

print(f"Average coordination number: {avg_coord:.2f}")
