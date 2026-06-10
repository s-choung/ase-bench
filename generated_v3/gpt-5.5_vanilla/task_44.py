from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111("Cu", size=(2, 2, 4), vacuum=10.0)

fixed_tags = [3, 4]
fixed_indices = [a.index for a in slab if a.tag in fixed_tags]
pos_before = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()

opt = BFGS(slab, logfile="bfgs.log")
opt.run(fmax=0.02)

pos_after = slab.positions[fixed_indices].copy()
disp = np.linalg.norm(pos_after - pos_before, axis=1)

print("fixed tags:", fixed_tags)
print("fixed indices:", fixed_indices)
print("positions before:")
print(pos_before)
print("positions after:")
print(pos_after)
print("displacements:")
print(disp)
print("max displacement:", disp.max())
print("unchanged:", np.allclose(pos_before, pos_after))
