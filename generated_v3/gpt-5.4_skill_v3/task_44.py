from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

fixed_indices = [i for i, atom in enumerate(slab) if atom.tag > 2]
pos_before = slab.get_positions()[fixed_indices].copy()

slab.calc = EMT()
opt = BFGS(slab, logfile='opt.log', trajectory='opt.traj')
opt.run(fmax=0.05)

pos_after = slab.get_positions()[fixed_indices].copy()

print('fixed_indices:', fixed_indices)
print('positions_before:')
print(pos_before)
print('positions_after:')
print(pos_after)
print('displacements:')
print(pos_after - pos_before)
print('all_fixed_unchanged:', np.allclose(pos_before, pos_after))
