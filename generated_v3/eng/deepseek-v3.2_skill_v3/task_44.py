from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
atoms.calc = EMT()

for i, atom in enumerate(atoms):
    atom.tag = i // 4

constraint = FixAtoms(mask=[tag <= 1 for tag in atoms.get_tags()])
atoms.set_constraint(constraint)

fixed_indices = [i for i, tag in enumerate(atoms.get_tags()) if tag <= 1]
initial_positions = atoms.positions[fixed_indices].copy()

opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.05)

final_positions = atoms.positions[fixed_indices]
displacements = final_positions - initial_positions

print("Fixed atom indices:", fixed_indices)
print("\nInitial positions of fixed atoms (Å):")
print(initial_positions)
print("\nFinal positions of fixed atoms (Å):")
print(final_positions)
print("\nDisplacements (Å):")
print(displacements)
print("\nMaximum displacement (Å):", abs(displacements).max())
