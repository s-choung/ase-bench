from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create N2 molecule
n2 = molecule('N2')
n2.calc = EMT()

# Optimize the geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()

# Print the frequencies
print(frequencies)
