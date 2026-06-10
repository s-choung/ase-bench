import numpy as np
from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Build Cu(111) 4-layer slab (2x2 surface cell, 10 Å vacuum)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Assign tags based on layers (sorted by z)
order = np.argsort(slab.positions[:, 2])
tags = np.zeros(len(slab), int)
tag = 0
prev_z = None
tol = 1e-3
for idx in order:
    z = slab.positions[idx, 2]
    if prev_z is None or abs(z - prev_z) > tol:
        tag += 1
        prev_z = z
    tags[idx] = tag
slab.set_tags(tags)

# Fix bottom two layers (tags 1 and 2)
mask = slab.get_tags() <= 2
slab.set_constraint(FixAtoms(mask=mask))

# Store positions of fixed atoms before optimization
fixed_before = slab.get_positions()[mask].copy()

# Attach EMT calculator and run BFGS optimization
slab.calc = EMT()
opt = BFGS(slab, trajectory='cu_opt.traj')
opt.run(fmax=0.05)

# Store positions after optimization
fixed_after = slab.get_positions()[mask].copy()

# Compare
print("Fixed atoms positions before optimization:\n", fixed_before)
print("\nFixed atoms positions after optimization:\n", fixed_after)
print("\nDid fixed atoms move? (allclose within 1e-4):", np.allclose(fixed_before, fixed_after, atol=1e-4))
