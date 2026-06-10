from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Cu(111) 4‑layer slab, 2×2 surface, 10 Å vacuum
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag atoms by layer (bottom two layers → tag 1, others → tag 0)
n_per_layer = len(slab) // 4
tags = [1 if i < 2 * n_per_layer else 0 for i in range(len(slab))]
slab.set_tags(tags)

# Build mask for fixed atoms and attach constraint
mask = np.array(slab.get_tags()) == 1
slab.set_constraint(FixAtoms(mask=mask))

# Store fixed atoms coordinates before optimisation
fixed_before = slab.positions[mask].copy()

# EMT calculator + BFGS relaxation
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.01)

# Coordinates after optimisation
fixed_after = slab.positions[mask]

# Verify that fixed atoms did not move
max_disp = np.max(np.linalg.norm(fixed_after - fixed_before, axis=1))
print("Fixed atoms before optimisation:\n", fixed_before)
print("\nFixed atoms after optimisation:\n", fixed_after)
print(f"\nMaximum displacement of fixed atoms: {max_disp:.3e} Å")
