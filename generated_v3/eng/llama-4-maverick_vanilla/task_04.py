from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2o = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
h2o.calc = EMT()

print('Initial energy:', h2o.get_potential_energy())

opt = BFGS(h2o)
opt.run(fmax=0.05)

print('Optimized energy:', h2o.get_potential_energy())
