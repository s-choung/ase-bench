from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLengths
from ase.geometry import distance

# Create an H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.75]])

# Set the EMT calculator
h2.calc = EMT()

# Calculate initial bond length and energy
initial_bond_length = distance(h2.positions[0], h2.positions[1])
initial_energy = h2.get_potential_energy()

# Apply FixBondLength constraint
constraint = FixBondLengths([(0, 1, 0.9)])
h2.set_constraint(constraint)

# Calculate adjusted bond length and energy
final_bond_length = distance(h2.positions[0], h2.positions[1])
final_energy = h2.get_potential_energy()

# Output results
print(f"Initial bond length: {initial_bond_length:.2f} Å, Energy: {initial_energy:.2f} eV")
print(f"Final bond length: {final_bond_length:.2f} Å, Energy: {final_energy:.2f} eV")
