import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Build 4-layer Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, orthogonal=True)

# Tag bottom 2 layers by z-coordinate (fix atoms with tag 0 or 1)
z_coords = slab.positions[:, 2]
z_layers = np.unique(z_coords)
slab.set_tags([0 if z < z_layers[2] else 1 if z < z_layers[3] else 2 for z in z_coords])

# Apply constraint to fix bottom 2 layers
constraint = FixAtoms(tag=[0, 1])
slab.set_constraint(constraint)

# Store initial positions of fixed atoms
fixed_indices = [i for i, tag in enumerate(slab.get_tags()) if tag in [0, 1]]
initial_fixed_pos = slab.positions[fixed_indices].copy()

# Run BFGS optimization
calc = EMT()
slab.calc = calc
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# Get final positions of fixed atoms
final_fixed_pos = slab.positions[fixed_indices]

# Compare positions
print("Initial positions of fixed atoms:\n", initial_fixed_pos)
print("\nFinal positions of fixed atoms:\n", final_fixed_pos)
print("\nDisplacement:", np.linalg.norm(final_fixed_pos - initial_fixed_pos, axis=1))
