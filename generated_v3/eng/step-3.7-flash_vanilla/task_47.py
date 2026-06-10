from ase.build import fcc
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = fcc('Cu', a=3.61).repeat((3, 3, 3))
nl = NeighborList(natural_cutoffs(atoms), self_interaction=False, bothways=True)
nl.update(atoms)
print(sum(len(nl.get_neighbors(i)[0]) for i in range(len(atoms))) / len(atoms))
