from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), a=3.615, vacuum=10.0)
slab.set_tags([1 if atom.z < slab.positions[:, 2].max() - 1.5 else 0 for atom in slab])
fixed_indices = [atom.index for atom in slab if atom.tag == 1]
constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)
slab.calc = EMT()
initial_pos = slab.positions[fixed_indices].copy()
opt = BFGS(slab)
opt.run(fmax=0.01)
final_pos = slab.positions[fixed_indices].copy()
print("Fixed atoms initial positions:\n", initial_pos)
print("Fixed atoms final positions:\n", final_pos)
print("Max displacement:", np.max(np.abs(final_pos - initial_pos)))
