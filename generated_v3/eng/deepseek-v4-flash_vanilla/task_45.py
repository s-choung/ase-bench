from ase import Atoms
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT
import numpy as np

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()
print("Before constraint:")
print(f"Bond length: {h2.get_distance(0, 1):.3f} Å")
print(f"Energy: {h2.get_potential_energy():.3f} eV")

constraint = FixBondLength(0, 1, length=0.9)
h2.set_constraint(constraint)
h2.set_distance(0, 1, 0.9)
print("\nAfter constraint:")
print(f"Bond length: {h2.get_distance(0, 1):.3f} Å")
print(f"Energy: {h2.get_potential_energy():.3f} eV")
