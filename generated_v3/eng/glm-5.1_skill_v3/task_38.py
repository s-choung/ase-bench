import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build and optimize 3x3x3 supercell of FCC Cu
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

# Calculate vibrational frequencies at Gamma point
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()

# Filter out acoustic and imaginary modes (near-zero or negative energies)
vib_energies = vib_energies[vib_energies > 1e-4]

# Compute Helmholtz free energy at 300 K using HarmonicThermo
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {F:.4f} eV")

vib.clean()
