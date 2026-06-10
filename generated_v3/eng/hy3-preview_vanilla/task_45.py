from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLengths

# Create H2 molecule with initial bond length 0.7 Å
h2 = Atoms('H2', positions=[[0, 0, 0], [0.7, 0, 0]])

# Set calculator and calculate initial state
h2.calc = EMT()
initial_energy = h2.get_potential_energy()
initial_bond = h2.get_distance(0, 1)

# Apply bond length constraint (0.9 Å)
constraint = FixBondLengths([(0, 1)], bondlength=0.9)
h2.set_constraint(constraint)

# Adjust positions to satisfy constraint
h2.positions[1, 0] = 0.9  # Set bond length to 0.9 Å

# Calculate final state
final_energy = h2.get_potential_energy()
final_bond = h2.get_distance(0, 1)

# Output results
print(f"Initial: Bond length = {initial_bond:.3f} Å, Energy = {initial_energy:.3f} eV")
print(f"Final:   Bond length = {final_bond:.3f} Å, Energy = {final_energy:.3f} eV")
