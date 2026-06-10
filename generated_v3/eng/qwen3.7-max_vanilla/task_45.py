from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()

print(f"Before: Bond Length = {atoms.get_distance(0, 1):.2f} Å, Energy = {atoms.get_potential_energy():.3f} eV")

atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLength(0, 1))

print(f"After:  Bond Length = {atoms.get_distance(0, 1):.2f} Å, Energy = {atoms.get_potential_energy():.3f} eV")
