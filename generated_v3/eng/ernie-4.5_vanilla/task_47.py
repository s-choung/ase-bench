from ase.build import bulk
from ase.calculators.neighborlist import NeighborList, natural_cutoffs
from ase.calculators.emt import EMT  # EMT is used implicitly for cutoffs in this context, but not as the energy calculator

# Create FCC copper 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True).repeat((3, 3, 3))

# Use natural cutoffs based on EMT (or other calculator-defined cutoffs)
calculator = EMT()  # Instantiate EMT to access its cutoffs; not for energy calculation here
cutoffs = natural_cutoffs(atoms, calculator)  # Get natural cutoff distances

# Build neighbor list
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate the number of neighbors for each atom
coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

# Calculate and print the average coordination number
average_coordination = sum(coordination_numbers) / len(coordination_numbers)
print(f"Average coordination number: {average_coordination:.2f}")
