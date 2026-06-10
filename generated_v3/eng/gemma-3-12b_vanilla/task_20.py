from ase.build import fcc
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

ntube_size = 6
tube_length = 4
a = 2.5

atoms = fcc(size=(ntube_size, ntube_size, tube_length), symbol='C', a=a)

for i in range(len(atoms)):
    atoms.set_constraint(FixAtoms(mask=[False] * 3))
    atoms.get_constraint().mask[i] = True

calc = EMT()
atoms.calc = calc

opt = BFGS(atoms, trajectory='tube.traj')
opt.run(fmax=0.02)

print(f"Number of atoms: {len(atoms)}")
print(atoms.cell)
