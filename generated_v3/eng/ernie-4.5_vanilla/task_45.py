from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Initialize H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0.76, 0, 0]])  # Approximate initial positions

# Print initial bond length
initial_bond_length = h2.get_distance(0, 1)
print(f"Initial bond length: {initial_bond_length:.4f} Ang")

# Calculate and print initial energy
h2.set_calculator(EMT())
initial_energy = h2.get_potential_energy()
print(f"Initial energy: {initial_energy:.4f} eV")

# Apply bond length constraint
constraint = FixBondLength(0, 1, 0.9)  # Fix bond length at 0.9 Angstrom
h2.set_constraint(constraint)

# Print bond length after constraint (should still be ~0.9 Ang, but we set it explicitly here)
# Note: Since the constraint fixes the bond length but doesn't change the actual positions without relaxation,
# we directly set the bond length to 0.9 to simulate the effect of the constraint (as relaxation isn't performed here).
h2.positions[1, 0] = h2.positions[0, 0] + 0.9
print(f"Bond length after applying constraint: {h2.get_distance(0, 1):.4f} Ang")

# Calculate and print energy after bond length constraint
energy_after_constraint = h2.get_potential_energy()
print(f"Energy after applying constraint: {energy_after_constraint:.4f} eV")
