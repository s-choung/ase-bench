from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()
slab.set_tags([1 if a.pos[2] > slab.positions[:, 2].min() + 0.2 else 0 for a in slab])
slab.set_constraint(FixAtoms(mask=[a.tag == 0 for a in slab]))

coords_before = slab.positions[slab.get_tags() == 0].copy()
BFGS(slab).run(fmax=0.01)
coords_after = slab.positions[slab.get_tags() == 0]

print("Fixed atoms before:\n", coords_before)
print("Fixed atoms after:\n", coords_after)
print("Fixed atoms moved:", (coords_before != coords_after).any())
