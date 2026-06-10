from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Build a 4‑layer Cu(111) slab (2×2 in‑plane) with vacuum
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Fix bottom two layers (tags 1 and 2)
mask = [atom.tag <= 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Attach EMT calculator
slab.calc = EMT()

# Indices of fixed atoms
fixed_idx = [i for i, a in enumerate(slab) if a.tag <= 2]
init_pos = slab.positions[fixed_idx].copy()

# Run BFGS optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# Positions after optimization
final_pos = slab.positions[fixed_idx]

# Output comparison
print("Fixed atom indices:", fixed_idx)
print("Initial positions (Å):\n", init_pos)
print("Final positions (Å):\n", final_pos)
print("Maximum displacement (Å):", np.max(np.abs(final_pos - init_pos)))
