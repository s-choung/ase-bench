import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

for atom in slab:
    if atom.tag == 1:
        atom.z += 0.2

mask = [a.tag >= 3 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

fixed_idx = [i for i, m in enumerate(mask) if m]
pos_before = slab.positions[fixed_idx].copy()

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

pos_after = slab.positions[fixed_idx]

print("Fixed atom indices:", fixed_idx)
print("Coordinates before optimization:\n", pos_before)
print("Coordinates after optimization:\n", pos_after)
print("Max displacement of fixed atoms:", np.max(np.abs(pos_after - pos_before)))
