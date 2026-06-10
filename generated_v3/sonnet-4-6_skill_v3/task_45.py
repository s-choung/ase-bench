from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
import numpy as np

h2 = molecule('H2')
h2.calc = EMT()

d_before = h2.get_distance(0, 1)
e_before = h2.get_potential_energy()
print(f"Before constraint:")
print(f"  Bond length: {d_before:.4f} Å")
print(f"  Energy: {e_before:.4f} eV")

h2_constrained = molecule('H2')
pos = h2_constrained.get_positions()
center = pos.mean(axis=0)
pos[0] = center + np.array([0.45, 0, 0])
pos[1] = center - np.array([0.45, 0, 0])
h2_constrained.set_positions(pos)

h2_constrained.set_constraint(FixBondLength(0, 1))
h2_constrained.calc = EMT()

d_after = h2_constrained.get_distance(0, 1)
e_after = h2_constrained.get_potential_energy()
print(f"\nAfter constraint (bond fixed at 0.9 Å):")
print(f"  Bond length: {d_after:.4f} Å")
print(f"  Energy: {e_after:.4f} eV")
