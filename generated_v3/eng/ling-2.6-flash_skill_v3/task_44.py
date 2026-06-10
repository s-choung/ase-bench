from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=False)

# Tag bottom 2 layers (two complete planes) for fixing
# fcc111(111) has close-packed layers along [11-20], here indexed by z
z_positions = slab.positions[:, 2]
sorted_indices = sorted(range(len(z_positions)), key=lambda i: z_positions[i])
natoms = len(slab)
layers = 4
per_layer = natoms // layers
fixed_indices = sorted_indices[:2 * per_layer]

# Apply FixAtoms constraint based on tags
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Attach EMT calculator
slab.calc = EMT()

# Store before positions of fixed atoms
pos_before = slab.positions[fixed_indices].copy()

# BFGS optimization
opt = BFGS(slab)
opt.run(fmax=0.05, steps=200)

# Store after positions of fixed atoms
pos_after = slab.positions[fixed_indices].copy()

# Print comparison
print("Fixed atoms coordinates before optimization:")
print(pos_before)
print("\nFixed atoms coordinates after optimization:")
print(pos_after)
print("\nMax displacement of fixed atoms:")
print(abs(pos_after - pos_before).max())
