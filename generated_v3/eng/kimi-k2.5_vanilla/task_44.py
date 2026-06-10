from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
tags = slab.get_tags()
fixed_indices = np.where(tags <= 2)[0]

initial_pos = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()

print("Running BFGS optimization...")
BFGS(slab, logfile=None).run(fmax=0.05)

final_pos = slab.positions[fixed_indices]

print("\nFixed atoms coordinate comparison:")
print(f"{'Index':<6} {'Initial Z':<12} {'Final Z':<12} {'Max Diff':<12}")
for idx, init, final in zip(fixed_indices, initial_pos, final_pos):
    max_diff = np.max(np.abs(final - init))
    print(f"{idx:<6} {init[2]:<12.6f} {final[2]:<12.6f} {max_diff:<12.2e}")
