from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 1.0)])
h2.calc = EMT()
e1 = h2.get_potential_energy()
d1 = h2.get_distance(0, 1)
print(f"Before constraint: bond = {d1:.3f} Å, energy = {e1:.3f} eV")

constraint = FixBondLength(0, 1, 0.9)
h2.constraints = [constraint]
constraint.adjust_positions(h2, h2.positions)
e2 = h2.get_potential_energy()
d2 = h2.get_distance(0, 1)
print(f"After constraint: bond = {d2:.3f} Å, energy = {e2:.3f} eV")
