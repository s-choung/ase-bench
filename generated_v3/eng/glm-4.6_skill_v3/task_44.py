from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Create Cu(111) slab with 4 layers
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Set calculator
slab.calc = EMT()

# Get coordinates of atoms in bottom 2 layers (tag >= 2) before optimization
fixed_mask = [a.tag >= 2 for a in slab]
fixed_indices = [i for i, mask in enumerate(fixed_mask) if mask]
coords_before = slab.positions[fixed_indices].copy()

# Apply constraint to fix bottom 2 layers
slab.set_constraint(FixAtoms(mask=fixed_mask))

# Run optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# Get coordinates after optimization
coords_after = slab.positions[fixed_indices]

# Compare coordinates
print("Coordinates comparison for fixed atoms:")
print("Before optimization:")
print(coords_before)
print("\nAfter optimization:")
print(coords_after)
print("\nMaximum displacement (Å):", np.max(np.abs(coords_after - coords_before)))
