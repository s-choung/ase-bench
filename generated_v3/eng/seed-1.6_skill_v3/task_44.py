from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(2,2,4), vacuum=10.0)

# Fix bottom 2 layers via tags
fix_mask = [a.tag < 2 for a in slab]
slab.set_constraint(FixAtoms(mask=fix_mask))

# Save initial positions of fixed atoms
fixed_indices = np.where(fix_mask)[0]
initial_fixed_pos = slab.positions[fixed_indices].copy()

# Optimize with EMT and BFGS
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# Get final positions of fixed atoms
final_fixed_pos = slab.positions[fixed_indices]

# Compare and print results
max_diff = np.abs(initial_fixed_pos - final_fixed_pos).max()
print("Initial fixed atom positions:\n", initial_fixed_pos)
print("\nFinal fixed atom positions:\n", final_fixed_pos)
print(f"\nMaximum position difference (Å): {max_diff:.10f}")
print("Fixed atoms unchanged:" if max_diff < 1e-6 else "Fixed atoms moved!")
