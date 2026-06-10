from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build a Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Create a neighbor list using natural cutoffs
nl = NeighborList(natural_cutoffs(atoms), bothways=True, self_interaction=False)

nl.update(atoms)

# Calculate the number of neighbors for each atom
coordination_numbers = []
for i in range(len(atoms)):
    coordination_numbers.append(len(nl.get_neighbors(i)[0]))

average_coordination_number = sum(coordination_numbers) / len(coordination_numbers)
print("Average Coordination Number:", average_coordination_number)
