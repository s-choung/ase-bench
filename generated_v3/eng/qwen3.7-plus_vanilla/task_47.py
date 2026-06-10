from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

atoms = bulk('Cu', 'fcc', a=3.61).repeat((3, 3, 3))
nl = NeighborList(natural_cutoffs(atoms), self_interaction=False)
nl.update(atoms)

avg_cn = sum(len(nl.get_neighbors(i)[0]) for i in range(len(atoms))) / len(atoms)
print(f"Average coordination number: {avg_cn:.1f}")
