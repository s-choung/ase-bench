import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Cu(111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Tag bottom two layers via z-coordinates
positions = slab.get_positions()
z = positions[:, 2]
sorted_indices = np.argsort(z)
layers = 4
atoms_per_layer = len(slab) // layers
tags = [0] * len(slab)
for i in sorted_indices[:atoms_per_layer * 2]:
    tags[i] = 1
slab.set_tags(tags)

# Fix bottom two layers
slab.set_constraint(FixAtoms(mask=[t == 1 for t in tags]))

# EMT calculator and optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.01)

# Compare fixed atoms' positions
fixed_indices = np.where(slab.get_tags() == 1)[0]
orig = slab.get_positions()[fixed_indices]
new = slab.get_positions()[fixed_indices]
print("Fixed positions before/after:", orig, new)
print("Difference:", orig - new)
