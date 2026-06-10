import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import ase.units

# Reference lattice constant for Ag (Å)
a0 = 4.09

# 7 points within +/-5% of a0
a_vals = np.linspace(a0 * 0.95, a0 * 1.05, 7)

volumes, energies = [], []
for a in a_vals:
    ag = bulk('Ag', 'fcc', a=a, cubic=True)
    ag.calc = EMT()
    energies.append(ag.get_potential_energy())
    volumes.append(ag.get_volume())

# Birch‑Murnaghan EOS fit
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
B_GPa = B * ase.units.GPa          # convert eV/Å³ → GPa
a_eq = v0 ** (1/3)                # equilibrium cubic lattice constant

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
