from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Build the CH4 molecule
ch4 = molecule('CH4')

# Set the EMT calculator
ch4.calc = EMT()

# Optimize the structure
opt = BFGS(ch4)
opt.run(fmax=0.01)

# Perform the vibration calculation
vib = Vibrations(ch4, name='vib')
vib.run()

# Get the frequencies
frequencies = vib.get_frequencies()

# Print the real frequencies
print("Real Vibrational Frequencies (cm⁻¹):")
for freq in frequencies:
  if freq > 0:
    print(freq)
