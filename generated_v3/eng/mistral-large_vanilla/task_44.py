from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.set_tags([3, 3, 2, 2, 1, 1, 0, 0])
constraint = FixAtoms(mask=[t < 2 for t in slab.get_tags()])
slab.set_constraint(constraint)
slab.calc = EMT()

fixed_atoms = [atom.index for atom in slab if atom.tag < 2]
print("Before optimization - fixed atoms coordinates:")
for i in fixed_atoms:
    print(slab[i].position)

BFGS(slab).run(fmax=0.05)

print("\nAfter optimization - fixed atoms coordinates:")
for i in fixed_atoms:
    print(slab[i].position)
