from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Build a 4‑layer Cu(111) slab with vacuum
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Identify atoms in the bottom two layers (tags 0 and 1)
fixed_idx = [i for i, a in enumerate(slab) if a.tag < 2]

# Apply FixAtoms constraint based on the mask
mask = [a.tag < 2 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Store coordinates of the fixed atoms before relaxation
coords_before = slab.get_positions()[fixed_idx].copy()

# Attach EMT calculator and run BFGS optimization
slab.calc = EMT()
BFGS(slab).run(fmax=0.01)

# Coordinates after relaxation
coords_after = slab.get_positions()[fixed_idx]

# Print comparison
print("Fixed atoms (indices):", fixed_idx)
print("Coordinates before optimization (Å):")
print(np.round(coords_before, 6))
print("Coordinates after optimization (Å):")
print(np.round(coords_after, 6))
# Verify that the displacement is negligible
displacements = np.linalg.norm(coords_after - coords_before, axis=1)
print("Displacements (Å):", np.round(displacements, 6))
