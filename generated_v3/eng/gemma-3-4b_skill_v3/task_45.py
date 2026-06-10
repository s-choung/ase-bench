from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.calculators import EMT
from ase.positions import Projection
from ase.visualize import view

# Create a H2 molecule
h2 = molecule('H2')

# Set the EMT calculator
h2.calc = EMT()

# Apply the FixBondLength constraint
fix = FixBondLength(0, 1)
h2.set_constraint(fix)

# Optimize using BFGS
opt = BFGS(h2)
opt.run(fmax=0.01)

# Calculate the energy before constraint
energy_before = h2.get_potential_energy()

# Calculate the energy after constraint
energy_after = h2.get_potential_energy()

# Print the bond length and energy before and after constraint
print("Bond length before constraint:", h2.get_distance(0, 1))
print("Energy before constraint:", energy_before)
print("Bond length after constraint:", h2.get_distance(0, 1))
print("Energy after constraint:", energy_after)

#Visualize the structure
view(h2)
