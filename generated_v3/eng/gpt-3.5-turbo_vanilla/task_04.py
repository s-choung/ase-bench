from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create an H2O molecule
h2o= Atoms('H2O', positions=[(0, -0.1, 0), (0.7, 0.5, 0), (-0.7, 0.5, 0)])

# Set up the EMT calculator
h2o.set_calculator(EMT())

# Print the initial energy
print('Initial energy:', h2o.get_potential_energy())

# Optimize the geometry using BFGS
opt = BFGS(h2o)
opt.run(fmax=0.05)

# Print the final energy
print('Final energy:', h2o.get_potential_energy())
