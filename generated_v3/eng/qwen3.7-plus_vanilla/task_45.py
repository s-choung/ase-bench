from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = molecule('H2')
atoms.calc = EMT()

print(f"Before: bond length = {atoms.get_distance(0, 1):.3f} A, energy = {atoms.get_potential_energy():.3f} eV")

atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLength(0, 1))

print(f"After: bond length = {atoms.get_distance(0, 1):.3f} A, energy = {atoms.get_potential_energy():.3f} eV")
