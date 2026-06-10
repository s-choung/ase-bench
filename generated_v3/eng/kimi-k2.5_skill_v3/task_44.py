from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

fixed_mask = [a.tag <= 2 for a in slab]
fixed_idx = [i for i, m in enumerate(fixed_mask) if m]
initial = slab.positions[fixed_idx].copy()

slab.set_constraint(FixAtoms(mask=fixed_mask))
slab.calc = EMT()

BFGS(slab).run(fmax=0.05)

final = slab.positions[fixed_idx]
delta = final - initial

print("Fixed indices:", fixed_idx)
print("Initial:\n", initial)
print("Final:\n", final)
print("Diff:\n", delta)
print("Max displacement:", abs(delta).max())
