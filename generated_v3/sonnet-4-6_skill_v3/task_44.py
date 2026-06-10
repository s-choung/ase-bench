from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# tag: 1=bottom, 2, 3, 4=top
fixed_mask = [atom.tag <= 2 for atom in slab]
fixed_indices = [i for i, f in enumerate(fixed_mask) if f]

pos_before = slab.get_positions()[fixed_indices].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))
slab.calc = EMT()

opt = BFGS(slab, trajectory='cu111_opt.traj')
opt.run(fmax=0.05)

pos_after = slab.get_positions()[fixed_indices].copy()

print(f"{'Idx':>4} {'Symbol':>6} | {'Before (x,y,z)':>36} | {'After (x,y,z)':>36} | {'Max diff':>10}")
print("-" * 100)
for i, idx in enumerate(fixed_indices):
    b = pos_before[i]
    a = pos_after[i]
    diff = np.max(np.abs(a - b))
    sym = slab[idx].symbol
    print(f"{idx:>4} {sym:>6} | {b[0]:>11.6f} {b[1]:>11.6f} {b[2]:>11.6f} | {a[0]:>11.6f} {a[1]:>11.6f} {a[2]:>11.6f} | {diff:>10.2e}")

print()
print(f"All fixed atoms unchanged: {np.allclose(pos_before, pos_after, atol=1e-10)}")
