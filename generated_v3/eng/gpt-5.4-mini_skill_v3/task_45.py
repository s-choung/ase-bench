from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT

h2 = molecule('H2')
h2.calc = EMT()

r0 = h2.get_distance(0, 1)
e0 = h2.get_potential_energy()

h2.set_constraint(FixBondLength(0, 1))
h2.set_distance(0, 1, 0.9, fix=0)

r1 = h2.get_distance(0, 1)
e1 = h2.get_potential_energy()

print(f"Before constraint: bond length = {r0:.3f} Å, energy = {e0:.6f} eV")
print(f"After constraint:  bond length = {r1:.3f} Å, energy = {e1:.6f} eV")
