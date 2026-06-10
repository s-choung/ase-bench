from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Set tags: bottom 2 layers get tag 1 (fixed), top 2 get tag 0
tags = np.zeros(len(slab), dtype=int)
tags[-8:] = 1  # bottom 2 layers (8 atoms in 2x2x2)
slab.set_tags(tags)

# Apply constraint to fix atoms with tag 1
mask = [tag == 1 for tag in slab.get_tags()]
slab.set_constraint(FixAtoms(mask=mask))

# Save initial coordinates of fixed atoms
fixed_indices = [i for i, m in enumerate(mask) if m]
initial_coords = slab[fixed_indices].get_positions()

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.01)

# Get final coordinates of fixed atoms
final_coords = slab[fixed_indices].get_positions()

# Print comparison
print("Initial fixed atom coordinates:")
print(initial_coords)
print("\nFinal fixed atom coordinates:")
print(final_coords)
print("\nMax displacement of fixed atoms:", np.max(np.abs(initial_coords - final_coords)))
