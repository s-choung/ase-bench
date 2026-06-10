from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc') * (3, 3, 3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

total_neighbors = sum(len(nl.get_neighbors(i)[0]) for i in range(len(atoms)))
avg_cn = total_neighbors / len(atoms)

print(f"Average coordination number: {avg_cn}")
