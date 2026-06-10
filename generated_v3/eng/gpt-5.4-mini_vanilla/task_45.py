from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.9)])
h2.calc = EMT()

r0 = h2.get_distance(0, 1)
e0 = h2.get_potential_energy()
print(f"Before constraint: bond length = {r0:.3f} Å, energy = {e0:.6f} eV")

h2.set_constraint(FixBondLength(0, 1))
r1 = h2.get_distance(0, 1)
e1 = h2.get_potential_energy()
print(f"After constraint:  bond length = {r1:.3f} Å, energy = {e1:.6f} eV")
