from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

print("Before constraint:")
print("Bond length:", h2.get_distance(0, 1))
print("Energy:", h2.get_potential_energy())

h2.set_constraint(FixBondLength(0, 1))
h2.set_distance(0, 1, 0.9, fix=0)

print("\nAfter constraint:")
print("Bond length:", h2.get_distance(0, 1))
print("Energy:", h2.get_potential_energy())
