from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Define H2O molecule
h2o = Atoms('H2O', positions=[(0, 0, 0), (0, 1, 0), (1, 0, 0.5)])

# Set the calculator
h2o.calc = EMT()

# Set up and run vibrational analysis
vib = Vibrations(h2o)
vib.run()

# Get frequencies and convert units
frequencies = vib.get_frequencies()  # in cm^-1
energies = np.array(frequencies) * (1.23981e-4)  # convert to eV

# Print results
for i, freq in enumerate(frequencies):
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energies[i]:.5f} eV")

vib.clean()
