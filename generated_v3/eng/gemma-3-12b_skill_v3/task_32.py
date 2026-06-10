from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create an H2O molecule
h2o = molecule('H2O')

# Set the calculator
h2o.calc = EMT()

# Optimize the geometry
from ase.optimize import BFGS
opt = BFGS(h2o)
opt.run(fmax=0.05)

# Calculate vibrational modes
vib = Vibrations(h2o)
vib.run()

# Get frequencies in cm^-1 and eV
frequencies_cm = vib.get_frequencies()
frequencies_eV = frequencies_cm / 96.485  # Convert cm^-1 to eV

# Print the frequencies
print("Vibrational Modes:")
for i, freq_cm in enumerate(frequencies_cm):
    freq_eV = frequencies_eV[i]
    print(f"Mode {i+1}: Frequency = {freq_cm:.2f} cm^-1, Energy = {freq_eV:.3f} eV")
