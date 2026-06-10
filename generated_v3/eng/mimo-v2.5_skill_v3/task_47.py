import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
from ase import Atoms

# Build 3x3x3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# Get natural cutoffs for Cu
cutoffs = natural_cutoffs(atoms)

# Create neighbor list
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors per atom
neighbor_counts = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    neighbor_counts.append(len(indices))

# Calculate average coordination number
avg_coordination = np.mean(neighbor_counts)

print(f"Number of atoms: {len(atoms)}")
print(f"Average coordination number: {avg_coordination:.2f}")
print(f"Min: {min(neighbor_counts)}, Max: {max(neighbor_counts)}")
