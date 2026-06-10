from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np
slab = fcc111('Cu', (2,2,4), vacuum=10.0)
slab.set_constraint(FixAtoms(indices=[a.index for a in slab if a.tag < 2]))
slab.calc = EMT()
fixed = [a.index for a in slab if a.tag < 2]
pos0 = slab.positions[fixed].copy()
BFGS(slab).run(fmax=0.05)
pos1 = slab.positions[fixed]
print('Before:\n', pos0, '\nAfter:\n', pos1, '\nMoved:', not np.allclose(pos0, pos1))
