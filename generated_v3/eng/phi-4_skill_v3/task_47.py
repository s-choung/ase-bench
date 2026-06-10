from ase import Atoms
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs

# Step 1: Create a Cu FCC 3x3x3 supercell
cu_fcc = bulk('Cu', 'fcc', a=3.6)
supercell = make_supercell(cu_fcc, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], scale_atoms=True)

# Step 2: Set up a calculator with EMT
supercell.calc = EMT()

# Step 3: Define the NeighborList using natural_cutoffs
cutoffs = natural_cutoffs(supercell)
neighbor_list = NeighborList(cutoffs, self_interaction=False, bothways=True)
neighbor_list.update(supercell)

# Step 4: Get the number of neighbors for each atom
# Iterating over each atom to find its neighbors
coordination_numbers = []
for atom in supercell:
    indices, offsets = neighbor_list.get_neighbors(atom.index)
    coordination_numbers.append(len(indices))

# Step 5: Compute the average coordination number
average_coordination_number = sum(coordination_numbers) / len(coordination_numbers)

# Output the result
print(f'Average coordination number: {average_coordination_number:.2f}')
