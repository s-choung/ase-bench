from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

fixed = [atom.tag <= 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=fixed))

pos_before = slab.get_positions().copy()

BFGS(slab).run(fmax=0.05)

pos_after = slab.get_positions().copy()

fixed_idx = np.where(fixed)[0]
print("Fixed atom indices:", fixed_idx.tolist())
print("Max displacement of fixed atoms (Å):", np.max(np.linalg.norm(pos_after[fixed_idx] - pos_before[fixed_idx], axis=1)))
print("Before:\n", pos_before[fixed_idx])
print("After:\n", pos_after[fixed_idx])
