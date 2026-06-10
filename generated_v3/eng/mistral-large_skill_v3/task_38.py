from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

# Build and relax Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()  # eV

# Remove imaginary frequencies (if any)
real_mask = freqs > 0
vib_energies = vib_energies[real_mask]

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300K: {F:.6f} eV")
vib.clean()
