from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase import units
import numpy as np

# Cu bulk fcc
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)  # 2x2x2 supercell for vibrations
atoms.calc = EMT()

# Optimize cell + positions
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

# Vibrational frequencies (Gamma point only)
vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs_cm = vib.get_frequencies()  # cm^-1
vib.clean()

# Convert to eV
freqs_eV = freqs_cm * units.invcm

# HarmonicThermo (treats as isolated cluster)
thermo = HarmonicThermo(vib_energies=freqs_eV, atoms=atoms, geometry='nonlinear', symmetrynumber=1, spin=0)
F = thermo.get_helmholtz_energy(temperature=300, volume=atoms.get_volume())

print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
