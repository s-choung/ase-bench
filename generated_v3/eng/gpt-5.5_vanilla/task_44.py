import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111("Cu", size=(2, 2, 4), vacuum=10.0)

tags = slab.get_tags()
fixed_indices = np.where(tags >= 3)[0]
slab.set_constraint(FixAtoms(indices=fixed_indices))

pos_before = slab.positions[fixed_indices].copy()

slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.03)

pos_after = slab.positions[fixed_indices]
disp = np.linalg.norm(pos_after - pos_before, axis=1)

print("Fixed atoms: index tag  before(x y z)                  after(x y z)                   displacement")
for i, before, after, d in zip(fixed_indices, pos_before, pos_after, disp):
    print(f"{i:3d} {tags[i]:3d}  {before}  {after}  {d:.3e}")

print(f"\nMaximum fixed-atom displacement: {disp.max():.3e} Å")
