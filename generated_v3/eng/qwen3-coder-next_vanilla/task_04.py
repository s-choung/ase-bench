from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
water = Atoms('H2O', positions=[[0.0, 0.0, 0.0], [0.757, 0.586, 0.0], [-0.757, 0.586, 0.0]])

# Set EMT calculator
water.calc = EMT()

# Print initial energy
print(f"Initial energy: {water.get_total_energy():.6f} eV")

# Optimize using BFGS
optimizer = BFGS(water)
optimizer.run(fmax=0.05)

# Print final energy
print(f"Final energy: {water.get_total_energy():.6f} eV")
