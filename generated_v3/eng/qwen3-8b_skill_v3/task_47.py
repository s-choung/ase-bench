import ase
from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3,3,3))
cutoff = natural_cutoffs(atoms)
nl = NeighborList(cutoff, sorted=True)
nl.update(atoms)
counts = [len(nl.get_neighbors(i)) for i in range(len(atoms))]
avg = sum(counts) / len(counts)
print(f"Average coordination number: {avg}")
