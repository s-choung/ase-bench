from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)
slab.set_tags([1]*16 + [2]*16 + [3]*16 + [4]*16)

mask = slab.get_tags() <= 2
slab.set_constraint(FixAtoms(mask=mask))

calc = EMT()
slab.calc = calc

pos_before = slab.get_positions()[mask].copy()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

pos_after = slab.get_positions()[mask]

print("Fixed atoms before:\n", np.round(pos_before, 6))
print("Fixed atoms after:\n", np.round(pos_after, 6))
