from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
import numpy as np

h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
h2.calc = EMT()

d_before = h2.get_distance(0, 1)
e_before = h2.get_potential_energy()
print(f"Before constraint:")
print(f"  Bond length: {d_before:.4f} Å")
print(f"  Energy: {e_before:.4f} eV")

h2_fixed = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.9]])
h2_fixed.calc = EMT()
h2_fixed.set_constraint(FixBondLength(0, 1))

d_after = h2_fixed.get_distance(0, 1)
e_after = h2_fixed.get_potential_energy()
print(f"\nAfter constraint (fixed at 0.9 Å):")
print(f"  Bond length: {d_after:.4f} Å")
print(f"  Energy: {e_after:.4f} eV")

from ase.optimize import BFGS

opt = BFGS(h2_fixed, logfile=None)
opt.run(fmax=0.01)

d_opt = h2_fixed.get_distance(0, 1)
e_opt = h2_fixed.get_potential_energy()
print(f"\nAfter optimization with constraint:")
print(f"  Bond length: {d_opt:.4f} Å")
print(f"  Energy: {e_opt:.4f} eV")
print(f"  Constraint active: bond length fixed = {abs(d_opt - 0.9) < 1e-6}")
