#!/usr/bin/env python3
"""
Find Cu FCC equilibrium lattice constant, volume and bulk modulus
using EMT and EOS fitting (no GUI).
"""

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# initial Cu FCC cell (EMT works with default lattice ~3.6 Å)
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# generate volumes by scaling the cell
scale_factors = np.linspace(0.94, 1.06, 9)   # 9 points around 1.0
volumes, energies = [], []

for s in scale_factors:
    cu.set_cell(cu.get_cell() * s, scale_atoms=True)
    energies.append(cu.get_potential_energy())
    volumes.append(cu.get_volume())

# EOS fit (Birch-Murnaghan 3rd order)
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()                     # v0 in Å³, B in eV/Å³
B_GPa = B * 160.21766208                  # 1 eV/Å³ = 160.21766208 GPa
a0 = v0**(1/3)                             # lattice constant for cubic cell

print(f"Equilibrium lattice constant a0 = {a0:.4f} Å")
print(f"Equilibrium volume per unit cell V0 = {v0:.4f} Å³")
print(f"Bulk modulus B0 = {B_GPa:.2f} GPa")
