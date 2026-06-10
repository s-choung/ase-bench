from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])

# Set calculator
atoms.calc = EMT()

# Print before constraint
print('Before:')
print('Bond length:', atoms.get_distance(0, 1))
print('Energy:', atoms.get_potential_energy())

# Apply constraint
atoms.set_constraint(FixBondLength(0, 1, 0.9))

# Optimize positions (move atoms along constraint)
atoms.set_positions([[0, 0, 0], [0, 0, 0.9]])

# Print after constraint
print('After:')
print('Bond length:', atoms.get_distance(0, 1))
print('Energy:', atoms.get_potential_energy())
