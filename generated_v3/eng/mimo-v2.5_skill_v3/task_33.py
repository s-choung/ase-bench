import numpy as np
from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
ch4 = molecule('CH4')
ch4.calc = EMT()

# Optimize structure
opt = BFGS(ch4, logfile=None)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(ch4, name='ch4_vib')
vib.run()

# Get frequencies and filter real ones
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]  # Filter out imaginary (negative) frequencies

print(f"All frequencies (cm⁻¹): {freqs}")
print(f"\nReal frequencies (cm⁻¹): {np.sort(real_freqs)}")

vib.clean()
