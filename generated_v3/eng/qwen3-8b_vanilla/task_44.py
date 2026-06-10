import ase.build
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = ase.build.slab('Cu', (1,1,1), layers=4, vacuum=5.0, direction='z')
atoms_per_layer = len(slab) // 4
fixed_indices = list(range(atoms_per_layer * 2))
constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)
slab.calc = EMT()
fixed_atoms_before = [slab[i].position for i in fixed_indices]
dyn = BFGS(slab, trajectory='slab_opt.traj')
dyn.run(fmax=0.05)
fixed_atoms_after = [slab[i].position for i in fixed_indices]
print("Fixed atoms before optimization:")
for pos in fixed_atoms_before: print(pos)
print("\nFixed atoms after optimization:")
for pos in fixed_atoms_after: print(pos)
