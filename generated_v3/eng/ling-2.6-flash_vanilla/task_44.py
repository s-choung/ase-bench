from ase.build import fcc111
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(4, 4, 4), vacuum=4.0, orthogonal=False)
tags = slab.get_tags()
tags[slab.get_positions()[:, 2] <= slab.get_positions()[:, 2].argsort()[:2]] = 1
slab.set_tags(tags)

fixed = FixAtoms(mask=slab.get_tags() == 1)
slab.set_constraint(fixed)
slab.calc = EMT()

fixed_pos_before = slab[slab.get_tags() == 1].positions.copy()
print("Fixed atoms before optimization:\n", fixed_pos_before)

opt = BFGS(slab)
opt.run(fmax=1e-08)

fixed_pos_after = slab[slab.get_tags() == 1].positions.copy()
print("Fixed atoms after optimization:\n", fixed_pos_after)

print("Atoms fixed:\n", np.allclose(fixed_pos_before, fixed_pos_after))
