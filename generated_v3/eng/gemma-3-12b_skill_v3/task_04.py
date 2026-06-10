from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create an H2O molecule
h2o = molecule('H2O')

# Set the EMT calculator
h2o.calc = EMT()

# Print the energy before optimization
print("Energy before optimization:", h2o.get_potential_energy())

# Optimize the geometry using BFGS
opt = BFGS(h2o)
opt.run(fmax=0.05)

# Print the energy after optimization
print("Energy after optimization:", h2o.get_potential_energy())
