from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Build CH4 and assign EMT calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Geometry optimization
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='ch4')
vib.run()
freqs = vib.get_frequencies()                # cm⁻¹
real_freqs = freqs[freqs > 0]                # filter out imaginary (negative) modes

print('Real vibrational frequencies (cm⁻¹):')
print(real_freqs)

vib.clean()                                  # remove temporary files
