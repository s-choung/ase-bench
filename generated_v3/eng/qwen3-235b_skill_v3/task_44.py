from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Create 4-layer Cu(111) slab with vacuum
slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0)

# Tag atoms: bottom layer=1, middle=2, top=3, topmost=4
slab.set_tags([1, 1, 2, 3])

# Fix atoms with tag 1 (bottom 2 layers conceptually, but only 1st layer here in 4-layer)
mask = [a.tag == 1 for a in slab]
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)

# Assign EMT calculator
slab.calc = EMT()

# Store coordinates of fixed atoms before optimization
fixed_indices = [i for i, m in enumerate(mask) if m]
before_coords = slab.positions[fixed_indices].copy()

# Run BFGS optimization
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# Get coordinates after optimization
after_coords = slab.positions[fixed_indices]

# Print comparison
for i, idx in enumerate(fixed_indices):
    print(f"Atom {idx}: Before {before_coords[i]} -> After {after_coords[i]}")
