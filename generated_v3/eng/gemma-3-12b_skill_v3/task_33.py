from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create a methane molecule
methane = molecule('CH4')
methane.calc = EMT()

# Optimize the structure
from ase.optimize import BFGS
opt = BFGS(methane)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(methane, name='vib')
vib.run()

# Get the frequencies and filter out imaginary frequencies
frequencies = vib.get_frequencies()
real_frequencies = frequencies[np.isreal(frequencies)]

# Print the real frequencies
print("Real vibrational frequencies (cm-1):")
print(real_frequencies)
