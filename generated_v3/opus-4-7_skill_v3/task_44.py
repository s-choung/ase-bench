import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
mask = [a.tag >= 3 for a in slab]
fixed_idx = [i for i, m in enumerate(mask) if m]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

pos_before = slab.get_positions()[fixed_idx].copy()
BFGS(slab).run(fmax=0.05)
pos_after = slab.get_positions()[fixed_idx]

print("Fixed atom indices:", fixed_idx)
print("Max displacement of fixed atoms:", np.abs(pos_after - pos_before).max())
for i, idx in enumerate(fixed_idx):
    print(f"Atom {idx}: before={pos_before[i]}, after={pos_after[i]}")
