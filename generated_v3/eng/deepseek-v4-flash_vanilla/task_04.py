from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = molecule('H2O')
h2o.calc = EMT()

print('Energy before:', h2o.get_potential_energy())
opt = BFGS(h2o)
opt.run(fmax=0.01)
print('Energy after:', h2o.get_potential_energy())
