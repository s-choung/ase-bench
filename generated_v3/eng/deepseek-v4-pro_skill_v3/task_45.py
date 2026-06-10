from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
import numpy as np

h2 = molecule('H2')
h2.calc = EMT()

d0 = h2.get_distance(0, 1)
e0 = h2.get_potential_energy()
print(f"Before: bond length = {d0:.3f} Å, energy = {e0:.3f} eV")

target = 0.9
vec = h2.positions[1] - h2.positions[0]
unit_vec = vec / np.linalg.norm(vec)
h2.positions[1] = h2.positions[0] + unit_vec * target
h2.set_constraint(FixBondLength(0, 1))

d1 = h2.get_distance(0, 1)
e1 = h2.get_potential_energy()
print(f"After:  bond length = {d1:.3f} Å, energy = {e1:.3f} eV")
