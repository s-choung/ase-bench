from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

# Set up vibrations
vib = Vibrations(n2)
vib.run()

# Get frequencies in cm^-1
freqs = vib.get_frequencies().real  # Take real part
freqs_cm1 = np.array([f * 5.034e26 for f in freqs if f > 0])  # Convert to cm^-1

# Print vibrational frequencies
for f in freqs_cm1:
    print(f"{f:.2f} cm^-1")

vib.clean()
