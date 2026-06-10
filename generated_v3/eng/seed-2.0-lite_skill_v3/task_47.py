from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.615).repeat((3, 3, 3))

# Create neighbor list with natural covalent cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, bothways=True, skin=0.0)
nl.update(atoms)

# Calculate coordination number for each atom
coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
average_cn = sum(coordination_numbers) / len(coordination_numbers)

# Print result
print(f"Average coordination number: {average_cn:.2f}")
