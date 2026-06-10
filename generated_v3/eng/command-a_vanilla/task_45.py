from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

# Define H2 molecule
h2 = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])

# Set EMT calculator
h2.calc = EMT()

# Calculate initial energy and bond length
initial_energy = h2.get_potential_energy()
initial_bond_length = h2.get_distance(0, 1)

# Apply FixBondLength constraint
h2.set_constraint(FixBondLength(0, 1, 0.9))

# Relax or recalculate with constraint
h2.get_potential_energy()

# Calculate final bond length and energy
final_bond_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()

# Print results
print(f"Initial bond length: {initial_bond_length:.4f} Å, Energy: {initial_energy:.4f} eV")
print(f"Final bond length: {final_bond_length:.4f} Å, Energy: {final_energy:.4f} eV")
