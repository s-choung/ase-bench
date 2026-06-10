from ase.build import fcc
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.io import write

calc = EMT()
atoms = fcc('Cu', size=3, sympret='abc')
atoms.calc = calc

filter_lj = atoms.get_cell_filter(size=10.0)

optimizer = BFGS(atoms, Trajectory='cu_opt.traj')
optimizer.set(fmax=0.01)
optimizer.attach(filter_lj)
optimizer.run(fmax=0.01)

print("Before optimization:")
print(atoms.get_cell_size())
print(atoms.get_potential_energy())

print("\nAfter optimization:")
print(atoms.get_cell_size())
print(atoms.get_potential_energy())

write('cu_optimized.xyz', atoms)
