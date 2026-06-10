from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
h2o = molecule('H2O')
h2o.calc = EMT()

# Print initial energy
print('Initial energy (eV):', h2o.get_potential_energy())

# Optimize with BFGS
opt = BFGS(h2o)
opt.run(fmax=0.05)

# Print final energy
print('Final energy (eV):', h2o.get_potential_energy())
