from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLengths # ASE uses FixBondLengths for bond constraints

atoms = molecule('H2')
atoms.calc = EMT()

print(f"Before: d = {atoms.get_distance(0, 1):.4f} Å, E = {atoms.get_potential_energy():.4f} eV")

atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLengths([(0, 1)]))

print(f"After:  d = {atoms.get_distance(0, 1):.4f} Å, E = {atoms.get_potential_energy():.4f} eV")
