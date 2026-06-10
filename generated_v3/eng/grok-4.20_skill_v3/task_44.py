from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(4,4,4), vacuum=6.0)
slab.set_tags([4]*(16) + [3]*(16) + [2]*(16) + [1]*(16))
slab.calc = EMT()
constraint = FixAtoms(mask=[tag >= 3 for tag in slab.get_tags()])
slab.set_constraint(constraint)

print('Before optimization:')
print(slab.positions[constraint.index])

opt = BFGS(slab)
opt.run(fmax=0.05)

print('After optimization:')
print(slab.positions[constraint.index])
