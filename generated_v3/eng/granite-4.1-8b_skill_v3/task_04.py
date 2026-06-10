from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule with optimized geometry
water = Atoms('H2O', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, -1.0]])

# Set the EMT calculator
water.calc = EMT()

# Print initial energy
print('Initial energy:', water.get_potential_energy())

# Optimize geometry using BFGS
optimizer = BFGS(water)
optimizer.run(fmax=0.05)

# Print final energy after optimization
print('Final energy:', water.get_potential_energy())
