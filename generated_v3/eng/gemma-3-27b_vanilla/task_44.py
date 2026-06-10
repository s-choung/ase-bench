from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT

atoms = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

tags = [0] * len(atoms)
for i in range(len(atoms)):
    if atoms.positions[i, 2] < atoms.cell[2, 2] * 2:
        tags[i] = 1

constraint = FixAtoms(tags=tags)
atoms.set_constraint(constraint)

calc = EMT()
atoms.set_calculator(calc)

initial_positions = [atom.position for atom in atoms if atom.tag == 1]

dyn = BFGS(atoms, trajectory='cu_slab_opt.traj')
dyn.run(fmax=0.02)

final_positions = [atom.position for atom in atoms if atom.tag == 1]

for i in range(len(initial_positions)):
    print(f"Atom {i}:")
    print(f"  Initial: {initial_positions[i]}")
    print(f"  Final: {final_positions[i]}")
    print(f"  Difference: {final_positions[i] - initial_positions[i]}")
