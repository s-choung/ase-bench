from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# 4‑layer Cu(111) slab, 2×2 lateral size, 10 Å vacuum
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom two layers (based on z coordinate)
z = slab.get_positions()[:, 2]
layer_z = np.unique(np.round(z, 5))
bottom_z = np.sort(layer_z)[:2]                     # two lowest z values
tags = np.isin(z, bottom_z)
slab.set_tags(np.where(tags, 1, 0))

# Mask of atoms to be fixed
fixed_mask = slab.get_tags() == 1
fixed_before = slab.positions[fixed_mask].copy()

# Apply constraint, attach calculator and optimise
slab.set_constraint(FixAtoms(mask=fixed_mask.tolist()))
slab.calc = EMT()
BFGS(slab, trajectory='opt.traj').run(fmax=0.01)

fixed_after = slab.positions[fixed_mask]

print('Fixed atoms before optimisation:\n', fixed_before)
print('Fixed atoms after optimisation:\n', fixed_after)
print('Maximum displacement of fixed atoms (Å):',
      np.max(np.linalg.norm(fixed_after - fixed_before, axis=1)))
