from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a Cu FCC bulk and expand to 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (3, 3, 3)

# Initialize NeighborList using natural_cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate coordination number for each atom
coordination_numbers = [len(nl.get_neighbors(i)) for i in range(len(atoms))]
avg_coord = sum(coordination_numbers) / len(atoms)

print(f"Average Coordination Number: {avg_coord:.2f}")
