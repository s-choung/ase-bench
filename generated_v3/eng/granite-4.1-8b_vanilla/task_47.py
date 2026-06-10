from ase import Atoms
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a Cu FCC lattice and form a 3x3x3 supercell
a = 3.615  # Cu lattice constant in Å
cell = [(0, 0, 0), (a/2, a/2, 0), (a/2, 0, a/2)]
atoms = Atoms('Cu', cell=cell, pbc=True)
atoms.set_positions([[x, y, z] for x in range(3) for y in range(3) for z in range(3)] * a / 3)
atoms = atoms * (3, 3, 3)

# Set a calculator (EMT) though it's not used for neighbor calculations
atoms.calc = EMT()

# Compute natural cutoffs for Cu
cutoffs = natural_cutoffs(atoms, update_positions=True)

# Create a NeighborList with the computed cutoffs
nl = NeighborList(cutoffs, skin=0.1, bothways=True, self_interaction=False)
nl.update(atoms)

# Calculate the number of neighbors for each atom
neighbors = nl.get_neighbors(atoms)

# Calculate the average coordination number
coordination_numbers = [len(n) for n in neighbors]
avg_coordination = sum(coordination_numbers) / len(coordination_numbers)

# Print the average coordination number
print(f"Average coordination number: {avg_coordination:.2f}")
