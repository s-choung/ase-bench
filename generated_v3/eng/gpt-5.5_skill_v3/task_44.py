import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111("Cu", size=(2, 2, 4), a=3.6, vacuum=10.0)

tags = slab.get_tags()
bottom_tags = sorted(set(tags))[-2:]
fixed_indices = [i for i, tag in enumerate(tags) if tag in bottom_tags]

before = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(indices=fixed_indices))
slab.calc = EMT()

BFGS(slab, logfile=None).run(fmax=0.02, steps=200)

after = slab.positions[fixed_indices].copy()
disp = np.linalg.norm(after - before, axis=1)

print("Fixed atom coordinates before and after optimization")
print("index tag   before_x   before_y   before_z    after_x    after_y    after_z    displacement")
for i, idx in enumerate(fixed_indices):
    b = before[i]
    a = after[i]
    print(f"{idx:5d} {tags[idx]:3d}  {b[0]:9.5f} {b[1]:9.5f} {b[2]:9.5f}  "
          f"{a[0]:9.5f} {a[1]:9.5f} {a[2]:9.5f}  {disp[i]:12.6e}")

print(f"\nBottom layer tags fixed: {bottom_tags}")
print(f"Maximum fixed-atom displacement: {disp.max():.6e} Angstrom")
