from ase.build import bulk
from ase.neighborlist import NeighborList
from ase.data import covalent_radii
import numpy as np

# Create FCC Cu and make 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)

# Calculate covalent radii-based cutoffs with default factor (1.1)
cutoffs = covalent_radii[atoms.get_atomic_numbers()] * 1.1
nl = NeighborList(cutoffs, skin=0.0, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate coordination numbers
coordination = np.zeros(len(atoms))
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination[i] = len(indices)

# Compute and print average coordination
avg_coord = np.mean(coordination)
print(f"Average coordination number: {avg_coord:.2f}")
