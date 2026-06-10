from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
atoms.calc = EMT()
initial_bond = atoms.get_distances(0, 1)
initial_energy = atoms.get_potential_energy()
print(f"Before: bond = {initial_bond:.3f} Å, energy = {initial_energy:.3f} eV")

atoms.set_constraint(FixBondLength(0, 1, 0.9))
BFGS(atoms).run(fmax=0.01)

final_bond = atoms.get_distances(0, 1)
final_energy = atoms.get_potential_energy()
print(f"After:  bond = {final_bond:.3f} Å, energy = {final_energy:.3f} eV")
