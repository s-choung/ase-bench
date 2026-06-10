from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Build Cu(111) 4-layer slab, 3x3 supercell
slab = fcc111('Cu', size=(3,3,4), vacuum=10, orthogonal=True)
n_layers = 4
slab.wrap()  # ensure PBC

# Assign tags by layer (bottom=1, top=4)
z_positions = slab.positions[:,2]
layers = np.unique(np.round(z_positions, 8))
layer_dict = dict(zip(sorted(layers), range(1, n_layers+1)))
tags = [layer_dict[round(z,8)] for z in z_positions]
slab.set_tags(tags)

# Fix atoms in bottom two layers (tags 1 and 2)
fixed_mask = [t in (1,2) for t in slab.get_tags()]
slab.set_constraint(FixAtoms(mask=fixed_mask))

# Store original positions of fixed atoms
fixed_indices = [i for i, f in enumerate(fixed_mask) if f]
fixed_coords_before = slab.positions[fixed_indices].copy()

# Set calculator & optimize
slab.calc = EMT()
dyn = BFGS(slab, logfile=None)
dyn.run(fmax=0.02)

# Store positions after optimization
fixed_coords_after = slab.positions[fixed_indices]

# Print and compare
for i, idx in enumerate(fixed_indices):
    print("Atom index:", idx)
    print("Before:", fixed_coords_before[i])
    print("After: ", fixed_coords_after[i])
    print("Moved? ", not np.allclose(fixed_coords_before[i], fixed_coords_after[i]), '\n')
