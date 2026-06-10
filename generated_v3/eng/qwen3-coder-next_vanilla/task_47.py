from ase import Atoms
from ase.build import bulk
from ase.neighborlist import neighbor_list
import numpy as np

# Create Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.61)
supercell = cu * (3, 3, 3)

# Build neighbor list with natural cutoffs
cutoffs = neighbor_list('r', supercell, cutoff=None)

# Calculate number of neighbors for each atom
numbers = supercell.get_atomic_numbers()
n_atoms = len(numbers)
neighbor_counts = np.zeros(n_atoms, dtype=int)

# Get indices for each atom
i_indices, j_indices = neighbor_list('ij', supercell, cutoff=None)
for i in i_indices:
    neighbor_counts[i] += 1

# Calculate average coordination number
avg_coordination = np.mean(neighbor_counts)

print(f"Average coordination number: {avg_coordination:.2f}")
