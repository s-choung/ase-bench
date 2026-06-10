from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
fix_mask = [a.tag < 2 for a in slab]
slab.set_constraint(FixAtoms(mask=fix_mask))

fixed_idx = np.where(fix_mask)[0]
print(f"Number of fixed atoms (bottom 2 layers): {len(fixed_idx)}\n")

pos_before = slab.get_positions()[fixed_idx].copy()

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

pos_after = slab.get_positions()[fixed_idx]

print("Fixed atom positions BEFORE optimization:")
print(pos_before)
print("\nFixed atom positions AFTER optimization:")
print(pos_after)
print(f"\nMax coordinate change: {np.abs(pos_after - pos_before).max():.2e} Å")
print(f"All fixed atoms unchanged: {np.allclose(pos_before, pos_after)}")
