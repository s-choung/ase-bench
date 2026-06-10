from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
median_z = sum(a.position[2] for a in slab) / len(slab)
slab.set_tags([1 if a.position[2] < median_z else 0 for a in slab])
slab.set_constraint(FixAtoms(mask=[a.tag == 1 for a in slab]))

fixed_idx = [i for i, a in enumerate(slab) if a.tag == 1]
initial_pos = slab.positions[fixed_idx].copy()

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

final_pos = slab.positions[fixed_idx]
print("Initial positions of fixed atoms:\n", initial_pos)
print("Final positions of fixed atoms:\n", final_pos)
print("Did fixed atoms move?", not np.allclose(initial_pos, final_pos))
