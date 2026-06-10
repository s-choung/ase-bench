from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Build 4-layer Cu(111) slab with tags: top=0,1,2,3=bottom
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Fix bottom 2 layers (tags 2 and 3) based on tags
fixed_indices = [a.index for a in slab if a.tag >= 2]
slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()

# Store positions of fixed atoms before optimization
pos_before = slab.positions[fixed_indices].copy()

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Positions after optimization
pos_after = slab.positions[fixed_indices]

# Compare
print(f"\nFixed atom indices: {fixed_indices}")
print(f"\nPositions BEFORE optimization:\n{pos_before}")
print(f"\nPositions AFTER optimization:\n{pos_after}")
print(f"\nMax displacement of fixed atoms: {abs(pos_after - pos_before).max():.2e} Å")
print("Fixed atoms did not move." if abs(pos_after - pos_before).max() < 1e-10 else "WARNING: fixed atoms moved!")
