from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', size=(3, 3, 3), cubic=True)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.build(atoms)
neighbors = nl.get_neighbors()
coordination_numbers = [len(neighbors[i][0]) for i in range(len(atoms))]
average = sum(coordination_numbers) / len(coordination_numbers)
print(average)
