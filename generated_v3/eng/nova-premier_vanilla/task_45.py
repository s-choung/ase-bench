from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.2]])
h2.calc = EMT()

print("Initial bond length:", h2.get_distance(0, 1))
e_init = h2.get_potential_energy()
print("Initial energy:", e_init / units.kJ * units.mol)

c = FixBondLength(0, 1, 0.9)
h2.set_constraint(c)

e_constrained = h2.get_potential_energy()
print("Constrained bond length:", h2.get_distance(0, 1))
print("Constrained energy:", e_constrained / units.kJ * units.mol)
