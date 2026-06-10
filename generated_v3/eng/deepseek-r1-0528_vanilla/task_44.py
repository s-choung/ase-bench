from ase import Atom, Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=7.0)
z_positions = slab.get_positions()[:, 2]
z_unique = np.unique(z_positions.round(decimals=3))
z_cutoff = (z_unique[1] + z_unique[2]) / 2
tags = np.where(z_positions < z_cutoff, 1, 0)
slab.set_tags(tags)
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.tag == 1])
slab.set_constraint(constraint)

fixed_before = [atom.position.copy() for atom in slab if atom.tag == 1]

slab.calc = EMT()
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

fixed_after = [atom.position for atom in slab if atom.tag == 1]
moved = any(not np.allclose(a, b) for a, b in zip(fixed_before, fixed_after))
print(f"Fixed atoms moved: {moved}")
