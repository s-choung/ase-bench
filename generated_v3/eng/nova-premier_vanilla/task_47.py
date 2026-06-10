from ase import Atoms, NeighborList
from ase.lattice.cubic import FaceCenteredCubic

atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                           symbol='Cu', size=(3, 3, 3), pbc=True)

nl = NeighborList(natural_cutoffs(atoms), self_interaction=False, bothways=True)
nl.update(atoms)

avg_cn = sum(len(nl.get_neighbors(i)[0]) for i in range(len(atoms))) / len(atoms)
print(f"Average coordination: {avg_cn:.2f}")
