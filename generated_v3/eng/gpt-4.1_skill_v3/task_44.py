from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Build 2x2x4 Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Fix bottom 2 layers (tag >= 3)
slab.set_constraint(FixAtoms(mask=[a.tag >= 3 for a in slab]))

# Get indices of fixed atoms
fixed_indices = [i for i, a in enumerate(slab) if a.tag >= 3]
init_pos = slab.positions[fixed_indices].copy()

# Optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# Check final positions
final_pos = slab.positions[fixed_indices]

# Compare
print("Fixed atom coordinates before optimization:")
print(init_pos)

print("\nFixed atom coordinates after optimization:")
print(final_pos)

print("\nDifference (should be ~0):")
print(final_pos - init_pos)
