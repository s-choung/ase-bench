from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build 3x3x3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3,3,3))

# Set up NeighborList
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors for each atom
counts = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    counts.append(len(indices))

avg_coord = sum(counts) / len(counts)
print(f'Average coordination number: {avg_coord:.2f}')
