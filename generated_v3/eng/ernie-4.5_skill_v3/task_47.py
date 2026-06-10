from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs

# Create Cu FCC 3x3x3 supercell and attach EMT calculator
atoms = bulk('Cu', 'fcc', cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

# Build neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms)  # Get natural cutoffs for all elements
neighbor_list = NeighborList(cutoffs, skin=0.3, self_interaction=False)
neighbor_list.update(atoms)

# Calculate and print average coordination number
coordination_numbers = []
for i in range(len(atoms)):
    neighbors, _ = neighbor_list.get_neighbors(i)
    coordination_numbers.append(len(neighbors))

average_coordination = sum(coordination_numbers) / len(coordination_numbers)
print(f"Average coordination number: {average_coordination:.2f}")
