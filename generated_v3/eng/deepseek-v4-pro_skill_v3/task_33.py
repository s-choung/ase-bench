from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Build and optimize CH4
atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Frequency calculation
vib = Vibrations(atoms, name='ch4_vib')
vib.run()
freqs = vib.get_frequencies()   # real(cm-1) and imag(cm-1) as a single array
# Filter only real (positive) frequencies
real_freqs = freqs[freqs > 0]
print("Real frequencies (cm⁻¹):", np.round(real_freqs, 2))
vib.clean()
