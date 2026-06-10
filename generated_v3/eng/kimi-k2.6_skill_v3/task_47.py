from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
nl = NeighborList(natural_cutoffs(atoms), self_interaction=False, bothways=True)
nl.update(atoms)

coord = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg = sum(coord) / len(atoms)

print(f"Average coordination number: {avg:.2f}")
