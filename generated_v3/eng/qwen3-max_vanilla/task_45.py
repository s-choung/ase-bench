from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with initial bond length
h2 = Atoms('H2', positions=[(0, 0, 0), (0.74, 0, 0)])
h2.calc = EMT()

# Print initial bond length and energy
initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()
print(f"Before constraint: bond length = {initial_bond_length:.3f} Å, energy = {initial_energy:.3f} eV")

# Apply constraint to fix bond length at 0.9 Å
h2.set_distance(0, 1, 0.9, fix=True)
h2.set_constraint(FixBondLength(0, 1))

# Recalculate energy with constraint
constrained_energy = h2.get_potential_energy()
constrained_bond_length = h2.get_distance(0, 1)
print(f"After constraint: bond length = {constrained_bond_length:.3f} Å, energy = {constrained_energy:.3f} eV")
