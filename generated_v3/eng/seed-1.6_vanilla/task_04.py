from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = molecule('H2O')
h2o.calc = EMT()

# Print initial energy
print('Initial energy:', h2o.get_potential_energy(), 'eV')

# Optimize with BFGS
opt = BFGS(h2o, logfile=None)
opt.run(fmax=0.01)

# Print final energy
print('Final energy:', h2o.get_potential_energy(), 'eV')
