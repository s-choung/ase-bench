from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a 3x3x3 FCC copper supercell
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_supercell = cu_bulk * (3, 3, 3)

# Initialize the NeighborList
cutoffs = natural_cutoffs(cu_supercell)
neighbor_list = NeighborList(cutoffs, self_interaction=False, bothways=True)
neighbor_list.update(cu_supercell)

# Calculate coordination numbers
coordination_numbers = []
for atom_index in range(len(cu_supercell)):
    indices, offsets = neighbor_list.get_neighbors(atom_index)
    coordination_numbers.append(len(indices))

# Print the average coordination number
average_coordination_number = sum(coordination_numbers) / len(cu_supercell)
print(f"Average coordination number: {average_coordination_number:.2f}")
