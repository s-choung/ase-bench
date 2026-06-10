from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Define initial hydrogen molecule with a bond length longer than desired
h2_atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.95)])

# Set up EMT calculator
h2 = EMT(h2_atoms)
h2_atoms.set_calculator(h2)

# Calculate initial energy and bond length
initial_energy = h2_atoms.get_potential_energy()
initial_distance = h2_atoms.get_distance(0, 1)

# Apply FixBondLength constraint to maintain bond length at 0.9 angstroms
constraint = FixBondLength(h2_atoms)  # Default bond length from initial guess
h2_atoms.set_constraint(constraint)

# Set up EMT calculator again
h2_atoms.set_calculator(h2)

# Calculate energy with bond length constraint applied
final_energy = h2_atoms.get_potential_energy()
final_distance = h2_atoms.get_distance(0, 1)

# Print results
print("Initial bond length: {:.2f} Å".format(initial_distance))
print("Initial energy: {:.2f} eV".format(initial_energy))
print("Final bond length: {:.2f} Å".format(final_distance))
print("Final energy: {:.2f} eV".format(final_energy))
