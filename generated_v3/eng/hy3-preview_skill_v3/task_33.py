from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Build CH4 molecule
atoms = molecule('CH4')

# Set calculator
atoms.calc = EMT()

# Optimize structure
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()

# Get frequencies and filter real ones
freqs = vib.get_frequencies()  # cm⁻¹
real_freqs = freqs[freqs > 0]

# Print real frequencies
print("Real vibrational frequencies (cm⁻¹):")
for i, freq in enumerate(real_freqs, 1):
    print(f"{i}: {freq:.2f}")

# Clean up vibration files
vib.clean()
