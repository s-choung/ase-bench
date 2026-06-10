from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

tags = slab.get_tags()
fixed_indices = [i for i, tag in enumerate(tags) if tag <= 2]
constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)

fixed_positions_before = slab[fixed_indices].get_positions().copy()

opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

fixed_positions_after = slab[fixed_indices].get_positions()

print("Fixed atom coordinates before optimization:")
for i, pos in zip(fixed_indices, fixed_positions_before):
    print(f"  Atom {i}: {pos}")

print("\nFixed atom coordinates after optimization:")
for i, pos in zip(fixed_indices, fixed_positions_after):
    print(f"  Atom {i}: {pos}")

print("\nMaximum displacement of fixed atoms:", 
      ((fixed_positions_after - fixed_positions_before)**2).sum(axis=1).max()**0.5)
