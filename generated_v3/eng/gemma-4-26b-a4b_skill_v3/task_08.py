import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup N2 molecule with EMT calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Geometry optimization (Crucial before vibration analysis)
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='n2_vib')
vib.run()

# Output frequencies in cm^-1
freqs = vib.get_frequencies()
print(f"Vibrational frequencies (cm^-1): {freqs}")

# Cleanup temporary files
vib.clean()
