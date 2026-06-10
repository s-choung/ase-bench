from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.units import Angstrom

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.7]])
h2.set_calculator(EMT())
print(f"Before: Bond length = {h2.get_distance(0, 1):.3f} Å, Energy = {h2.get_potential_energy():.3f} eV")

h2.set_constraint(FixBondLength(0, 1))
h2.positions[1][2] = 0.9 * Angstrom
print(f"After: Bond length = {h2.get_distance(0, 1):.3f} Å, Energy = {h2.get_potential_energy():.3f} eV")
