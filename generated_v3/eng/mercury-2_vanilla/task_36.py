#!/usr/bin/env python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# reference lattice constant for Ag FCC
a_ref = bulk('Ag', 'fcc').cell[0, 0]

# 7 lattice constants within ±5 %
a_vals = np.linspace(a_ref * 0.95, a_ref * 1.05, 7)
volumes = a_vals**3 / 4  # volume per atom for FCC

calc = EMT()
energies = []
for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.set_calculator(calc)
    energies.append(atoms.get_total_energy())

# Birch‑Murnaghan fit
v0, e0, B0 = EquationOfState(volumes, energies, eos='birch').fit()
a_eq = (4 * v0)**(1/3)                     # equilibrium lattice constant
B0_GPa = B0 * 160.2                       # convert eV/Å³ → GPa

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B0_GPa:.2f} GPa')
