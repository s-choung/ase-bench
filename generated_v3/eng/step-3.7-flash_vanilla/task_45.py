from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT
import numpy as np

h2 = molecule('H2')
h2.calc = EMT
print(f"Before: bond = {np.linalg.norm(h2.positions[0]-h2.positions[1]):.2f} Å, E = {h2.get_potential_energy():.2f} eV")

h2.set_constraint(FixBondLength(0, 1, length=0.9))
vec = h2.positions[1] - h2.positions[0]
h2.positions[1] = h2.positions[0] + vec / np.linalg.norm(vec) * 0.9
print(f"After: bond = {np.linalg.norm(h2.positions[0]-h2.positions[1]):.2f} Å, E = {h2.get_potential_energy():.2f} eV")
