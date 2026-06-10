from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create Cu(111) slab (4 layers)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# Assign tags based on layer index (bottom 2 layers = layers 0 and 1)
# fcc111 build orders atoms from top to bottom usually, 
# but we can identify them by z-coordinate.
z_coords = slab.get_positions()[:, 2]
z_min = min(z_coords)
z_max = max(z_coords)
# Identify atoms in the bottom 2 layers (roughly bottom half of the slab thickness)
# A more robust way for fcc111 is using the internal layer logic or simple z-cut
layers_z = sorted(list(set([round(z, 2) for z in z_coords])))
fixed_z = layers_z[:2] 

mask = [atom.position[2] not in fixed_z for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Get indices of fixed atoms to verify
fixed_indices = [i for i, m in enumerate(mask) if not m]
pos_before = slab.positions[fixed_indices].copy()

# Optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

pos_after = slab.positions[fixed_indices]

print("Fixed Atoms Indices:", fixed_indices)
print("\nCoordinates Before:\n", pos_before)
print("\nCoordinates After:\n", pos_after)
print("\nVerification: No movement =", (pos_before == pos_after).all())
