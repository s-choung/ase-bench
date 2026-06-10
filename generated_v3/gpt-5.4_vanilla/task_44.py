from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
tags = atoms.get_tags()
fixed_indices = [i for i, t in enumerate(tags) if t <= 2]

pos_before = atoms.get_positions().copy()
atoms.set_constraint(FixAtoms(indices=fixed_indices))
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.02)

pos_after = atoms.get_positions()
disp = pos_after[fixed_indices] - pos_before[fixed_indices]

print("fixed_indices:", fixed_indices)
print("max_abs_displacement_of_fixed_atoms:", np.abs(disp).max())
for i, d in zip(fixed_indices, disp):
    print(i, pos_before[i], pos_after[i], d)
