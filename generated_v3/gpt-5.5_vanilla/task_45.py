from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms("H2", positions=[(0, 0, 0), (0, 0, 0.74)])
h2.calc = EMT()

print("before bond length:", h2.get_distance(0, 1))
print("before energy:", h2.get_potential_energy())

h2.set_distance(0, 1, 0.9, fix=0)
h2.set_constraint(FixBondLength(0, 1))

print("after bond length:", h2.get_distance(0, 1))
print("after energy:", h2.get_potential_energy())
