from ase.build import bulk, make_supercell
from ase.neighborlist import natural_cutoffs, NeighborList
from ase import Atoms

# Create a Cu FCC bulk structure
cu = bulk('Cu', 'fcc')

# Create a 3x3x3 supercell
supercell = make_supercell(cu, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])

# Calculate natural cutoffs for the supercell
cutoffs = natural_cutoffs(supercell)
nc = NeighborList(cutoffs, self_interaction=False, bothways=True)
nc.update(supercell)

# Calculate the number of neighbors for each atom
coordination_numbers = [len(nc.get_neighbors(i)) for i in range(len(supercell))]

# Compute and print the average coordination number
average_coordination_number = sum(coordination_numbers) / len(supercell)
print(f"Average coordination number: {average_coordination_number:.2f}")
