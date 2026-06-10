from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

fixed_mask = slab.get_tags() >= 3
fixed_before = slab.positions[fixed_mask].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))
BFGS(slab).run(fmax=0.05)

fixed_after = slab.positions[fixed_mask].copy()

print("Fixed atoms before optimization:")
print(fixed_before)
print("\nFixed atoms after optimization:")
print(fixed_after)
print("\nMax displacement of fixed atoms:", np.max(np.abs(fixed_after - fixed_before)))
