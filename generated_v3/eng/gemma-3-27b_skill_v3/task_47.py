from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6, size=(3, 3, 3))
nl = NeighborList(atoms, cutoff=natural_cutoffs(atoms))
neighbors = [len(nl.neighbors(i)) for i in range(len(atoms))]
avg_coordination = sum(neighbors) / len(atoms)

print(f"Average coordination number: {avg_coordination}")
