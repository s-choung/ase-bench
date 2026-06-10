from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
nl = NeighborList(natural_cutoffs(atoms, 1.2), bothways=True, self_interaction=False)
nl.update(atoms)
cn = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(sum(cn) / len(atoms))
