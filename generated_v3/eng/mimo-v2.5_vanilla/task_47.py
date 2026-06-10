from ase.build import bulk
from ase.neighborlist import NeighborList

# Create 3x3x3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * [3, 3, 3]

# Build NeighborList using natural cutoffs (distance-based)
nl = NeighborList(natural_cutoffs=True, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors for each atom (exclude self-interactions)
neighbor_counts = []
for i in range(len(atoms)):
    neighbors = nl.get_neighbors(i)[0]  # Get indices of neighboring atoms
    neighbor_counts.append(len(neighbors))

# Calculate and print average coordination number
avg_coordination = sum(neighbor_counts) / len(neighbor_counts)
print(f"Average coordination number: {avg_coordination:.3f}")
