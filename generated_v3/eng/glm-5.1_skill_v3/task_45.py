from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = molecule('H2')
h2.calc = EMT()

print(f"Before constraint: Bond length = {h2.get_distance(0, 1):.4f} Å, Energy = {h2.get_potential_energy():.4f} eV")

h2.positions[1] = h2.positions[0] + [0, 0, 0.9]
h2.set_constraint(FixBondLength(0, 1))

print(f"After constraint:  Bond length = {h2.get_distance(0, 1):.4f} Å, Energy = {h2.get_potential_energy():.4f} eV")
