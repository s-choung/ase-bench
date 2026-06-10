import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 4‑layer Cu(111) slab
slab = fcc111('Cu', size=(1, 1, 4))

# Tag bottom two layers with tag=1
z = slab.positions[:, 2]
layers = np.unique(z)               # sorted list of layer heights
tags = np.zeros(len(slab), dtype=int)
tags[np.isin(z, layers[:2])] = 1    # bottom two layers
slab.set_tags(tags)

# Fix atoms with tag=1
slab.set_constraint(FixAtoms(tag=1))

# EMT calculator and BFGS optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.01)   # structural convergence criterion

# Coordinates of fixed atoms before and after optimization
fixed = slab.get_tags() == 1
init_pos = slab[fixed].positions.copy()
final_pos = slab[fixed].positions.copy()

print("Initial positions of fixed atoms:\n", init_pos)
print("Final positions of fixed atoms:\n", final_pos)
print("Max deviation:", np.max(np.linalg.norm(final_pos - init_pos, axis=1)))
