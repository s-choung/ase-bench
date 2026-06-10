from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

zs = slab.get_positions()[:, 2]
unique_zs = np.sort(np.unique(np.round(zs, 5)))
for i, z in enumerate(unique_zs):
    slab[np.abs(zs - z) < 0.01].set_tags(i)

fixed_mask = np.array([a.tag < 2 for a in slab])
slab.set_constraint(FixAtoms(mask=lambda a: a.tag < 2))
coords_before = slab.get_positions()[fixed_mask].copy()

slab.calc = EMT()
opt = BFGS(slab, logfile='opt.log')
opt.run(fmax=0.05)

coords_after = slab.get_positions()[fixed_mask].copy()

print('Fixed atoms unchanged:', np.allclose(coords_before, coords_after))
print('Max displacement:', np.max(np.abs(coords_after - coords_before)))
print('Before:\n', coords_before)
print('After:\n', coords_after)
