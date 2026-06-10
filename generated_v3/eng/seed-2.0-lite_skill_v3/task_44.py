from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Create 4-layer Cu(111) slab, 2x2 surface unit cell with 10Å vacuum
slab = fcc111('Cu', size=(2,2,4), vacuum=10.0)
# Identify indices of bottom 2 layers (tags = 1 (bottommost) and 2)
fixed_indices = [i for i, atom in enumerate(slab) if atom.tag <= 2]
# Save pre-optimization coordinates of fixed atoms
pre_fixed_coords = slab.positions[fixed_indices].copy()

# Apply FixAtoms constraint to bottom layers
slab.set_constraint(FixAtoms(indices=fixed_indices))
# Assign EMT calculator
slab.calc = EMT()

# Run BFGS optimization
opt = BFGS(slab, trajectory='cu111_relax.traj')
opt.run(fmax=0.05)

# Get post-optimization coordinates of fixed atoms
post_fixed_coords = slab.positions[fixed_indices]
# Calculate maximum displacement of fixed atoms
max_displacement = np.max(np.linalg.norm(post_fixed_coords - pre_fixed_coords, axis=1))

# Print comparison
print("\n=== Fixed Atoms Coordinate Comparison ===")
print("Pre-optimization fixed atom positions (Å):\n", pre_fixed_coords)
print("\nPost-optimization fixed atom positions (Å):\n", post_fixed_coords)
print(f"\nMaximum displacement of fixed atoms: {max_displacement:.6f} Å")
