from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# 4‑layer Cu(111) slab
slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0, periodic=True)

# tags set by fcc111 correspond to layer index (0 = bottom)
mask = slab.get_tags() < 2               # bottom 2 layers
slab.set_constraint(FixAtoms(mask=mask))

# store coordinates of the fixed atoms
fixed_idx = np.where(mask)[0]
init_coords = slab.positions[fixed_idx].copy()

# run BFGS optimization with EMT
slab.set_calculator(EMT())
BFGS(slab).run(fmax=0.01)

# coordinates after optimization
final_coords = slab.positions[fixed_idx]

# output
print("Fixed atoms coordinates before optimization:")
print(init_coords)
print("\nFixed atoms coordinates after optimization:")
print(final_coords)
print("\nDid any fixed atom move? ", not np.allclose(init_coords, final_coords, atol=1e-8))
