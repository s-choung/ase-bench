import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Build 4-layer Cu(111) slab (tags 0,1,2,3 correspond to layers)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Identify bottom 2 layers (tag 0 and 1) and store initial positions
fixed_indices = [atom.index for atom in slab if atom.tag < 2]
initial_pos = slab.get_positions()[fixed_indices].copy()

# Apply constraint and calculator
slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()

# Run optimization
BFGS(slab).run(fmax=0.05)

# Extract final positions and compare
final_pos = slab.get_positions()[fixed_indices]

print("Fixed atoms positions BEFORE optimization:")
print(initial_pos)
print("\nFixed atoms positions AFTER optimization:")
print(final_pos)
print(f"\nMax displacement of fixed atoms: {np.max(np.abs(final_pos - initial_pos)):.8f} Å")
