from ase import Atoms
from ase.neighborlist import NeighborList, natural_cutoffs
from ase.calculators.emt import EMT
import numpy as np

# Create Cu FCC 3x3x3 supercell
cu = Atoms('Cu', cell=[0, 0.5, 0.5, 0.5, III, 0.5, 0.5, 0.5, 0], pbc=True)
cu = cu.repeat((3, 3, 3))

# Apply EMT calculator to get reasonable cutoff behavior
cu.calc = EMT()

# Build NeighborList with natural cutoffs
cutoffs = natural_cutoffs(cu, mult=1.1)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(cu)

# Calculate neighbors per atom
neighbor_counts = []
for i in range(len(cu)):
    indices, offsets = nl.get_neighbors(i)
    neighbor_counts.append(len(indices))

# Compute and print average coordination
avg_coordination = np.mean(neighbor_counts)
print(f'Average coordination number: {avg_coordination:.2f}')
