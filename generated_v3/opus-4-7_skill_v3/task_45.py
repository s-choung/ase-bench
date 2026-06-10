from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

atoms = Atoms('H2', positions=[[0,0,0],[0,0,0.9]])
atoms.calc = EMT()

print(f"Before: bond = {atoms.get_distance(0,1):.4f} Å, E = {atoms.get_potential_energy():.4f} eV")

atoms.set_constraint(FixBondLength(0, 1))
BFGS(atoms).run(fmax=0.01)

print(f"After:  bond = {atoms.get_distance(0,1):.4f} Å, E = {atoms.get_potential_energy():.4f} eV")
