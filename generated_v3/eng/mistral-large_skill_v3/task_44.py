from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=3.6)
slab.set_tags([0, 0, 1, 1])
slab.calc = EMT()

fixed_mask = [a.tag == 0 for a in slab]
fixed_atoms_before = slab.positions[fixed_mask].copy()
slab.set_constraint(FixAtoms(mask=fixed_mask))

BFGS(slab).run(fmax=0.05)

fixed_atoms_after = slab.positions[fixed_mask]
print("Fixed atoms before optimization:")
print(fixed_atoms_before)
print("Fixed atoms after optimization:")
print(fixed_atoms_after)
print("Max displacement of fixed atoms:", ((fixed_atoms_after - fixed_atoms_before)**2).sum(axis=1).max()**0.5)
