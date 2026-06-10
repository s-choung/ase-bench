from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create an H2O molecule
h2o = molecule('H2O')
h2o.calc = EMT()

# Print initial energy
print('Initial energy:', h2o.get_potential_energy())

# Optimize the H2O molecule using BFGS
opt = BFGS(h2o)
opt.run(fmax=0.05)

# Print final energy
print('Final energy:', h2o.get_potential_energy())
