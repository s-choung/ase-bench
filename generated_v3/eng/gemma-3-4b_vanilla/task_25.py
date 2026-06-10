from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.build import FCC

calc = EMT(pseudize=True)
a = 3.61
atoms = FCC(a=a, color=[1, 0, 0], size=10)
atoms.set_calculator(calc)

constraints = FixAtoms(indices=[0])
atoms.set_constraint(constraints)

opt = BFGS(maximum_iterations=1000, convergence_tolerance=0.01)
opt.set_tolerance(0.01)

atoms, energy = opt.minimize(atoms)

print("Original cell size:", atoms.cell.a[0])
print("Original energy:", atoms.get_potential_energy())

print("Optimized cell size:", atoms.cell.a[0])
print("Optimized energy:", atoms.get_potential_energy())
