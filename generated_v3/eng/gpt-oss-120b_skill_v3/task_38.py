#!/usr/bin/env python3
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# bulk Cu, relax cell+positions
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

# supercell for phonons
supercell = atoms * (2, 2, 2)
supercell.calc = EMT()

# vibrational analysis
vib = Vibrations(supercell, name='cu_bulk')
vib.run()
energies = vib.get_energies()           # eV
vib.clean()

# Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib_energies=energies, atoms=supercell)
F = thermo.get_helmholtz_energy(temperature=300)  # eV

print(f'Helmholtz free energy (Cu bulk, 300 K): {F:.5f} eV')
