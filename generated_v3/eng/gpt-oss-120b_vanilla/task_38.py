#!/usr/bin/env python3
# Bulk Cu vibrational free energy (EMT)

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

# Build FCC Cu and attach EMT calculator
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()

# 2×2×2 supercell for phonon calculation
sup = cu * (2, 2, 2)

# Phonon analysis (finite displacement 0.01 Å)
ph = Phonons(sup, sup.calc, delta=0.01)
ph.run()                       # compute forces for displaced cells
freqs = ph.get_frequencies()   # frequencies in THz

# Exclude (near) zero modes
freqs = [f for f in freqs if f > 1e-5]

# Harmonic thermodynamics
thermo = HarmonicThermo(freqs)

# Helmholtz free energy at 300 K (eV)
F = thermo.get_helmholtz_energy(temperature=300)

print(f'Helmholtz free energy of bulk Cu at 300 K: {F:.6f} eV')
