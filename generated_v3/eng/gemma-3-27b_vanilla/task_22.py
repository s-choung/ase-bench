from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

atoms = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
n2 = molecule('N2')
n2.translate( (0,0,2.0) )

atoms += n2

fixed_layers = [atom.index for atom in atoms if atom.position[2] < atoms.cell[2,2]/2 ]
constraint = FixAtoms(indices=fixed_layers)
atoms.set_constraint(constraint)

calc = EMT()
atoms.set_calculator(calc)

dyn = BFGS(atoms, trajectory='AlN2.traj')
dyn.run(fmax=0.02)

print(f"Number of atoms: {len(atoms)}")
print(f"Atom types: {set([atom.symbol for atom in atoms])}")
