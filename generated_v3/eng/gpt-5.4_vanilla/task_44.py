from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Cu(111) 4-layer slab; ASE tags layers from top=1 to bottom=4 for fcc111
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
fixed_mask = slab.get_tags() >= 3  # bottom 2 layers: tags 3 and 4

before = slab.positions[fixed_mask].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))
slab.calc = EMT()

opt = BFGS(slab, logfile='-')
opt.run(fmax=0.01)

after = slab.positions[fixed_mask].copy()

print("Fixed atom indices:", np.where(fixed_mask)[0].tolist())
print("Coordinates before optimization:")
print(before)
print("Coordinates after optimization:")
print(after)
print("Displacements of fixed atoms:")
print(after - before)
print("Max |displacement|:", np.abs(after - before).max())
