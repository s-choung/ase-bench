from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
import numpy as np

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()

opt = LBFGS(atoms)
opt.run(fmax=0.01)

print('steps:', opt.get_number_of_steps())
print('energy:', atoms.get_potential_energy())
