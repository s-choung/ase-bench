from ase import Atoms
from ase.build import bulk, make_supercell
from ase.neighborlist import NeighborList, natural_cutoffs

cu = bulk('Cu', 'fcc', a=3.6)
supercell = make_supercell(cu, [[3,0,0], [0,3,0], [0,0,3]])
cutoffs = natural_cutoffs(supercell)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(supercell)

coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(supercell))]
avg_cn = sum(coordination_numbers) / len(coordination_numbers)
print(avg_cn)
