from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
atoms = bulk('Cu', 'fcc', cubic=True).repeat(3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)
coords = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(sum(coords) / len(coords))
