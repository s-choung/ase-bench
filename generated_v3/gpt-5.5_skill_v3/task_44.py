import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111("Cu", size=(2, 2, 4), a=3.615, vacuum=10.0)

mask = [atom.tag >= 3 for atom in slab]
fixed_indices = np.where(mask)[0]
pos_before = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

opt = BFGS(slab, logfile="-")
opt.run(fmax=0.05, steps=200)

pos_after = slab.positions[fixed_indices].copy()
disp = np.linalg.norm(pos_after - pos_before, axis=1)

print("fixed_indices:", fixed_indices.tolist())
print("fixed_tags:", [slab[i].tag for i in fixed_indices])
print("positions_before:\n", pos_before)
print("positions_after:\n", pos_after)
print("displacements_A:", disp)
print("max_displacement_A:", disp.max())
print("fixed_atoms_unchanged:", np.allclose(pos_before, pos_after, atol=1e-12))
