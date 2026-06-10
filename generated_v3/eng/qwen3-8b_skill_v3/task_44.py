import ase.build
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = ase.build.fcc111('Cu', size=(1, 1, 4), vacuum=10.0)
for i, atom in enumerate(slab): atom.tag = 1 if i < 2 else 0
constraint = FixAtoms(mask=[a.tag == 1 for a in slab])
slab.set_constraint(constraint)
slab.calc = EMT()

fixed_indices = [i for i, a in enumerate(slab) if a.tag == 1]
before = [slab.positions[i] for i in fixed_indices]

opt = BFGS(slab)
opt.run(fmax=0.05)

after = [slab.positions[i] for i in fixed_indices]

print("Before optimization:")
for i, pos in enumerate(before): print(f"Fixed atom {i}: {pos}")

print("\nAfter optimization:")
for i, pos in enumerate(after): print(f"Fixed atom {i}: {pos}")
