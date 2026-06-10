from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# fcc111 tags: bottom layer = nlayers, top layer = 1
# Fix bottom 2 layers (tags 3 and 4)
mask = slab.get_tags() >= 3
slab.set_constraint(FixAtoms(mask=mask))

fixed_idx = np.where(mask)[0]
pos_before = slab.positions[fixed_idx].copy()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

pos_after = slab.positions[fixed_idx]

print("Fixed atom indices:", fixed_idx)
print("\nPositions BEFORE optimization:")
print(pos_before)
print("\nPositions AFTER optimization:")
print(pos_after)
print(f"\nMax displacement of fixed atoms: {np.max(np.abs(pos_after - pos_before)):.2e} Å")
print(f"All fixed atoms stationary: {np.allclose(pos_before, pos_after)}")
