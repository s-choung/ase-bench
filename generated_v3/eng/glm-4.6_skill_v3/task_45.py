from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

e1 = h2.get_potential_energy()
d1 = h2.get_distance(0, 1)
print(f"Before: Energy = {e1:.3f} eV, Bond Length = {d1:.3f} Å")

h2.set_distance(0, 1, 0.9)
h2.set_constraint(FixBondLength(0, 1))

e2 = h2.get_potential_energy()
d2 = h2.get_distance(0, 1)
print(f"After:  Energy = {e2:.3f} eV, Bond Length = {d2:.3f} Å")
