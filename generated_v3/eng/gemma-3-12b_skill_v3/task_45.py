from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
import numpy as np

# Create an H2 molecule
atoms = Atoms('h2', positions=[(0.0, 0.0, 0.0), (0.9, 0.0, 0.0)])
atoms.calc = EMT()

# Get initial bond length and energy
initial_bond_length = atoms.get_distance(0, 1)
initial_energy = atoms.get_potential_energy()

print(f"Initial bond length: {initial_bond_length:.4f} Angstroms")
print(f"Initial energy: {initial_energy:.4f} eV")

# Apply FixBondLength constraint
constraint = FixBondLength(0, 1, 0.9)
atoms.set_constraint(constraint)

# Calculate energy after applying the constraint
final_energy = atoms.get_potential_energy()

# Get final bond length (should be 0.9 Angstroms, but check)
final_bond_length = atoms.get_distance(0, 1)

print(f"Final bond length: {final_bond_length:.4f} Angstroms")
print(f"Final energy: {final_energy:.4f} eV")
