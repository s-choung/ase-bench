from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Generate 4-layer Cu(111) slab with vacuum
slab = fcc111('Cu', size=(1,1,4), vacuum=10.0, orthogonal=True)

# Tag bottom 2 layers (smallest z) as 0, top 2 as 1
z = slab.positions[:, 2]
bot_layers = np.sort(np.unique(np.round(z, 6)))[:2]
slab.set_tags(np.where(np.isclose(z[:, None], bot_layers[None, :], atol=1e-5).any(1), 0, 1))

# Fix bottom layers via tags, set EMT calculator
slab.set_constraint(FixAtoms(tags=[0]))
slab.calc = EMT()

# Store initial fixed atom positions
fixed_mask = slab.get_tags() == 0
init_pos = slab.positions[fixed_mask].copy()

# Run BFGS optimization to 0.01 eV/Å force convergence
BFGS(slab).run(fmax=0.01)

# Compare and print results
final_pos = slab.positions[fixed_mask].copy()
print("Initial fixed atom positions (Å):\n", init_pos)
print("Final fixed atom positions (Å):\n", final_pos)
print("Max fixed atom displacement (Å):", np.max(np.linalg.norm(final_pos - init_pos, axis=1)))
