from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.set_tags([4 - i for i in slab.get_tags()])

fixed = [atom.tag >= 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=fixed))

pos_before = slab.get_positions().copy()

slab.calc = EMT()
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

pos_after = slab.get_positions().copy()

fixed_idx = np.where(fixed)[0]
print("Fixed atoms positions before optimization:")
print(pos_before[fixed_idx])
print("Fixed atoms positions after optimization:")
print(pos_after[fixed_idx])
print("Max displacement of fixed atoms:", np.max(np.abs(pos_after[fixed_idx] - pos_before[fixed_idx])))
