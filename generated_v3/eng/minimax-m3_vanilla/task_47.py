from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordination = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg = sum(coordination) / len(coordination)
print(f"Number of atoms: {len(atoms)}")
print(f"Average coordination number: {avg}")
