from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create the water molecule
water = Atoms('H2O', positions=[[0, 0, 0], [0, 0, 1.0], [0, 1.0, 0]])

# Assign the EMT calculator
water.calc = EMT()

# Print initial energy
print("Initial energy:", water.get_potential_energy())

# Perform optimization using BFGS
optimizer = BFGS(water)
optimizer.run(fmax=0.05)

# Print optimized energy
print("Optimized energy:", water.get_potential_energy())
