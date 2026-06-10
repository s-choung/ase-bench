#!/usr/bin/env python3
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# initial Cu fcc bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# generate EOS data
volumes, energies = [], []
scales = np.linspace(0.94, 1.06, 9)          # ≈ ±6 % around a0
for s in scales:
    a = atoms.copy()
    a.set_cell(atoms.get_cell() * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# fit Birch‑Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B_eV = eos.fit()                    # B in eV/Å³
B_GPa = B_eV / units.eV * units.Joule / (units.m**3) * 1e-9  # convert to GPa
# simpler conversion: 1 eV/Å³ = 160.21766208 GPa
B_GPa = B_eV * 160.21766208

print(f'Equilibrium volume per cell : {v0:.3f} Å³')
print(f'Bulk modulus                : {B_GPa:.2f} GPa')
