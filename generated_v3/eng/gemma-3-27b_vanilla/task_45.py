from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

h2 = molecule('H2')
print("Initial bond length:", h2.get_distances()[0])

calc = EMT()
h2.set_calculator(calc)
initial_energy = h2.get_potential_energy()
print("Initial energy:", initial_energy)

constraint = FixBondLength(0, 1, 0.9)
h2.set_constraint(constraint)

print("Bond length after constraint:", h2.get_distances()[0])
constrained_energy = h2.get_potential_energy()
print("Energy after constraint:", constrained_energy)
