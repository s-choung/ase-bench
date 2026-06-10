from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Cu', size=(2,2,4), vacuum=10.0)
mask = [a.tag <= 2 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()

fixed_idx = np.where(mask)[0]
pos_before = slab.positions[fixed_idx].copy()

BFGS(slab, logfile=None).run(fmax=0.05)

pos_after = slab.positions[fixed_idx]
print('Before:\n', pos_before)
print('After:\n', pos_after)
print('Moved:', not np.allclose(pos_before, pos_after))
