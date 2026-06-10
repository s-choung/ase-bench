from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Create a 3x3x3 supercell of Cu FCC
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Determine natural cutoffs
cutoffs = natural_cutoffs(atoms)

# Initialize the NeighborList
neighbor_list = NeighborList(cutoffs, self_interaction=False, bothways=True)
neighbor_list.update(atoms)

# Calculate and print the number of neighbors for each atom
coordination_numbers = [len(neighbor_list.get_neighbors(i)[0]) for i in range(len(atoms))]
average_coordination_number = np.mean(coordination_numbers)

print(f"Average Coordination Number: {average_coordination_number:.2f}")
