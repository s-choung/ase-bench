from ase.lattice.cubic import FaceCenteredCubic
from ase.neighborlist import natural_cutoffs, NeighborList

atoms = FaceCenteredCubic('Cu', size=(3, 3, 3))
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)
nums = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(sum(nums) / len(nums))
