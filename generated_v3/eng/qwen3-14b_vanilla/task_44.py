from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111('Cu', size=(4,4), layers=4, vacuum=10.0)
positions = slab.get_positions()
z = positions[:, 2]
sorted_indices = np.argsort(z)
mask = np.zeros(len(slab), dtype=bool)
mask[sorted_indices[:len(slab)//2]] = True
mask[sorted_indices[len(slab)//2:]] = True
slab.set_tags(mask.astype(int))
constraint = FixAtoms(mask=[tag == 1 for tag in slab.get_tags()])
slab.set_constraint(constraint)
slab.set_calculator(EMT())
opt = BFGS(slab)
opt.run(fmax=0.05)
fixed_initial = slab.get_positions()[np.array(slab.get_tags()) == 1]
fixed_final = slab.get_positions()[np.array(slab.get_tags()) == 1]
print("Initial fixed positions:\n", fixed_initial, "\nFinal fixed positions:\n", fixed_final)
