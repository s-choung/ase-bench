from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Create H2 molecule
h2 = Atoms([['H', (0, 0, 0)], ['H', (1.0, 0, 0)]])

# Calculate initial energy and bond length
emt = EMT()
h2.set_calculator(emt)
initial_energy = h2.get_potential_energy()
initial_bond_length = h2.get_distance(0, 1)

# Apply FixBondLength constraint
constraint = FixBondLength(indices=(0, 1), length=0.9)
h2.set_constraint(constraint)

# Calculate energy after applying constraint
h2.set_calculator(emt)
final_energy = h2.get_potential_energy()
final_bond_length = h2.get_distance(0, 1)

# Print results
print(f"Initial bond length: {initial_bond_length:.3f} Å")
print(f"Initial energy: {initial_energy:.6f} eV")
print(f"Final bond length: {final_bond_length:.3f} Å")
print(f"Final energy: {final_energy:.6f} eV")
