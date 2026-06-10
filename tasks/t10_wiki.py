"""T10 Wiki: Fix bottom 2 layers of a 4-layer Pt(111) slab using tags"""
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

z_positions = slab.positions[:, 2]
unique_z = np.unique(z_positions.round(2))
z_cutoff = unique_z[1]
mask = slab.positions[:, 2] <= z_cutoff + 0.1
slab.set_constraint(FixAtoms(mask=mask))

opt = BFGS(slab)
opt.run(fmax=0.05, steps=10)
n_fixed = sum(mask)
print(f"Relaxed. Energy: {slab.get_potential_energy():.4f} eV")
print(f"Fixed {n_fixed} of {len(slab)} atoms (bottom 2 layers)")
