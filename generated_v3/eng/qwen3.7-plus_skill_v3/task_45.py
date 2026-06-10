from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.9)])
atoms.calc = EMT()

print(f"Before: Bond Length = {atoms.get_distance(0, 1):.4f} A, Energy = {atoms.get_potential_energy():.4f} eV")

atoms.set_constraint(FixBondLength(0, 1))

print(f"After:  Bond Length = {atoms.get_distance(0, 1):.4f} A, Energy = {atoms.get_potential_energy():.4f} eV")
