import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

z_coords = slab.positions[:, 2]
z_sorted = np.sort(np.unique(np.round(z_coords, 4)))
for atom in slab:
    layer = np.argmin(np.abs(z_sorted - round(atom.position[2], 4)))
    atom.tag = layer + 1

mask = [atom.tag <= 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

fixed_idx = [i for i, m in enumerate(mask) if m]
pos_before = slab.get_positions()[fixed_idx].copy()

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

pos_after = slab.get_positions()[fixed_idx]

print("Fixed atom indices:", fixed_idx)
print("Max displacement of fixed atoms:", np.max(np.abs(pos_after - pos_before)))
for i, idx in enumerate(fixed_idx):
    print(f"Atom {idx} (tag={slab[idx].tag}):")
    print(f"  before: {pos_before[i]}")
    print(f"  after : {pos_after[i]}")
