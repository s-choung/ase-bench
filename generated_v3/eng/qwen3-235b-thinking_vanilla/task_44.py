from ase import build
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

atoms = build.fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
n_per_layer = 2 * 2
tags = [0] * (2 * n_per_layer) + [1] * (len(atoms) - 2 * n_per_layer)
atoms.set_tags(tags)

constraint = FixAtoms(mask=atoms.get_tags() == 0)
atoms.set_constraint(constraint)
atoms.calc = EMT()

fixed_mask = atoms.get_tags() == 0
initial_pos = atoms.positions[fixed_mask].copy()

opt = BFGS(atoms)
opt.run(fmax=0.05)

final_pos = atoms.positions[fixed_mask]
for i in range(len(initial_pos)):
    print(f"Fixed atom {i}:")
    print(f"  Initial: {initial_pos[i]}")
    print(f"  Final:   {final_pos[i]}")
