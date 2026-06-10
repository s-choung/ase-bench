from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
cutoffs = natural_cutoffs(atoms, mult=1.2)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coord_nums = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coord = sum(coord_nums) / len(atoms)
print(f"Average coordination number: {avg_coord:.2f}")
