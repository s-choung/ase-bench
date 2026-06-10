from ase.build import fcc111
from ase neighborlist import NeighborList, natural_cutoffs

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=0.0)
nl = NeighborList(natural_cutoffs(atoms), self_interaction=False, bothways=True)
nl.update(atoms)

coords = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
print(f"Average coordination number: {sum(coords) / len(coords):.2f}")
