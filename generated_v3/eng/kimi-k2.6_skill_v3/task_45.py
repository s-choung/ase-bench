from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.74]])
atoms.calc = EMT()
print(f"Before: bond length = {atoms.get_distance(0, 1):.3f} Å, energy = {atoms.get_potential_energy():.3f} eV")

atoms.set_positions([[0.0, 0.0, 0.0], [0.0, 0.0, 0.9]])
atoms.set_constraint(FixBondLength(0, 1))
print(f"After:  bond length = {atoms.get_distance(0, 1):.3f} Å, energy = {atoms.get_potential_energy():.3f} eV")
