from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Build 4-layer Cu(111) slab (2x2 lateral size, 10Å vacuum)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Fix bottom 2 layers using tag-based mask (tags 0 and 1 for lowest layers)
slab.set_constraint(FixAtoms(mask=[a.tag < 2 for a in slab]))

# Assign EMT calculator
slab.calc = EMT()

# Record fixed atom positions before optimization
fixed_mask = [a.tag < 2 for a in slab]
pos_before = slab.get_positions()[fixed_mask].copy()

# Run BFGS optimization
BFGS(slab).run(fmax=0.05)

# Get fixed atom positions after optimization
pos_after = slab.get_positions()[fixed_mask].copy()

# Print comparison and verify no movement
print("Fixed atom positions before optimization:\n", pos_before)
print("Fixed atom positions after optimization:\n", pos_after)
print("Maximum displacement of fixed atoms (Å):", np.max(np.abs(pos_after - pos_before)))
