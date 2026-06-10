from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create water molecule
h2o = molecule('H2O')
h2o.calc = EMT()

# Energy before optimization
E_before = h2o.get_potential_energy()
print(f'Energy before optimization: {E_before:.4f} eV')

# Optimize geometry
opt = BFGS(h2o)
opt.run(fmax=0.01)

# Energy after optimization
E_after = h2o.get_potential_energy()
print(f'Energy after optimization: {E_after:.4f} eV')
