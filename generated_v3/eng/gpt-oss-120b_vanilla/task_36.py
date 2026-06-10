#!/usr/bin/env python3
"""
EOS fitting for FCC Ag using ASE and EMT.
7 lattice constants within ±5 % of an initial guess.
Prints equilibrium lattice constant (Å) and bulk modulus (GPa).
"""

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# initial lattice constant guess (Å)
a_guess = 4.09

# generate 7 lattice constants spanning ±5 %
a_vals = [a_guess * (1 + delta) for delta in
         [ -0.05, -0.035, -0.02, 0.0, 0.02, 0.035, 0.05 ]]

volumes, energies = [], []

calc = EMT()                     # built‑in calculator
for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a)   # single unit cell
    atoms.set_calculator(calc)
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Birch‑Murnaghan EOS fit
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B_ev = eos.fit()          # B in eV/Å³
a0 = v0 ** (1/3)                  # equilibrium lattice constant

# conversion 1 eV/Å³ = 160.21766208 GPa
B_GPa = B_ev * 160.21766208

print(f'Equilibrium lattice constant a0 = {a0:.5f} Å')
print(f'Bulk modulus B0 = {B_GPa:.2f} GPa')
