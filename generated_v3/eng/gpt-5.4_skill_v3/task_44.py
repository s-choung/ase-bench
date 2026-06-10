from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
fixed_mask = [atom.tag > 2 for atom in slab]
fixed_indices = [i for i, m in enumerate(fixed_mask) if m]

before = slab.positions[fixed_indices].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

after = slab.positions[fixed_indices].copy()

print('Fixed atom indices:', fixed_indices)
print('Before optimization:')
print(before)
print('After optimization:')
print(after)
print('Displacements:')
print(after - before)
print('All fixed atoms unchanged:', np.allclose(before, after))
