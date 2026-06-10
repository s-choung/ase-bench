from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', (1, 1, 4), vacuum=10.0)
mask = [a.tag < 2 for a in slab]
fixed_indices = [i for i, m in enumerate(mask) if m]
before = slab.get_positions()[fixed_indices]
slab.set_constraint(FixAtoms(mask=mask))
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
after = slab.get_positions()[fixed_indices]
print('Before optimization:\n', before)
print('After optimization:\n', after)
