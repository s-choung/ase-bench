import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup CH4 molecule and calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Structure optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Vibrational frequency calculation
vib = Vibrations(atoms, name='ch4_vib')
vib.run()

# Get frequencies (cm^-1) and filter real ones (non-imaginary)
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]

print(f"Real frequencies (cm^-1): {real_freqs}")

# Cleanup temporary files
vib.clean()
