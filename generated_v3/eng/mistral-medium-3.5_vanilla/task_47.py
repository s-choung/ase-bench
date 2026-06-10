from ase.lattice.cubic import FaceCenteredCubic
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = FaceCenteredCubic('Cu', size=(3, 3, 3))
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)
coord_nums = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coord = sum(coord_nums) / len(atoms)
print(f"Average coordination number: {avg_coord:.2f}")
