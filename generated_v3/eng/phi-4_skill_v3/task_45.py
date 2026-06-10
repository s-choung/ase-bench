from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT
import numpy as np
from ase.visualize import view

# Create hydrogen molecule
h2 = Atoms('H2', positions=[(0, 0, 0) for _ in range(2)])

# Apply EMT calculator
h2.calc = EMT()

# Print the bond length and energy before applying the constraint
print("Before constraint:")
print("Bond length:", np.linalg.norm(np.array(h2.get_positions()[1]) - np.array(h2.get_positions()[0])))
print("Potential energy:", h2.get_potential_energy())

# Define EMT E2 constraint (bond 0 to 1 and fix the length at 0.9 Å)
constraint = FixBondLength(adsorbate=h2, index1=0, index2=1, bondlength=0.9)

# Apply the constraint
h2.set_constraint(constraint)

# Apply EMT calculator to constrained H2 molecule
h2.calc_energy()

# Print the bond length and energy after applying the constraint
print("\nAfter constraint:")
print("Bond length:", np.linalg.norm(np.array(h2.get_positions()[1]) - np.array(h2.get_positions()[0])))
print("Potential energy:", h2.get_potential_energy())

# Visualize the molecule using ase.visualize (optional)
view(h2)
