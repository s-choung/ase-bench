from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.615)

# Generate a 3x3x3 supercell
supercell = atoms.repeat(3)

# Define natural cutoffs for the supercell
cutoffs = natural_cutoffs(supercell, method='voronoi')

# Initialize NeighborList
nl = NeighborList(cutoffs, skin=0.1, self_interaction=False, bothways=True)
nl.update(supercell)

# Calculate the number of neighbors for each atom
coordination_numbers = [len(nl.get_neighbors(i, [0, 1])) for i in range(len(supercell))]

# Compute the average coordination number
average_coordination = sum(coordination_numbers) / len(coordination_numbers)
print(f"Average coordination number: {average_coordination:.2f}")
