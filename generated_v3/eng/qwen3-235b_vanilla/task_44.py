from ase import Atoms, Atom
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.center(axis=2)

# Assign tags: bottom 2 layers (tags 0,1), top 2 layers (tags 2,3)
slab.set_tags([atom.index // 4 for atom in slab])

# Fix bottom two layers (tag < 2)
mask = [tag < 2 for tag in slab.get_tags()]
fix_constraint = FixAtoms(mask=mask)
slab.set_constraint(fix_constraint)

# Store coordinates of fixed atoms before optimization
fixed_indices = [i for i, tag in enumerate(slab.get_tags()) if tag < 2]
before_coords = slab.positions[fixed_indices].copy()

# Attach EMT calculator
slab.calc = EMT()

# Optimize geometry
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.01)

# Get coordinates after optimization
after_coords = slab.positions[fixed_indices]

# Print comparison
for i, idx in enumerate(fixed_indices):
    print(f"Atom {idx}: Before {before_coords[i]} -> After {after_coords[i]}")
