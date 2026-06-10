from ase import Atoms, units
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Get natural cutoff distances
cutoffs = natural_cutoffs(atoms)

# Build NeighborList
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate coordination numbers
coordination_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

# Print average coordination number
avg_coordination = sum(coordination_numbers) / len(coordination_numbers)
print(f'Average coordination number: {avg_coordination:.2f}')
