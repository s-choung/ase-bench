from ase import Atoms
from ase.build import fcc111
from ase.neighborlist import NeighborList, natural_cutoffs

# Create Cu FCC 3x3x3 supercell
slab = fcc111('Cu', size=(3, 3, 3), vacuum=0)
cutoffs = natural_cutoffs(slab, mult=1.0)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(slab)

# Calculate coordination number for each atom
coordination_numbers = []
for i in range(len(slab)):
    indices = nl.get_neighbors(i)[0]
    coordination_numbers.append(len(indices))

# Print average coordination number
print(sum(coordination_numbers) / len(coordination_numbers))
