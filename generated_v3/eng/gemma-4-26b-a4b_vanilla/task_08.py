import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule (Using EMT for demonstration, though EMT is for metals)
# Note: EMT is typically for transition metals; for realistic N2, one would use a DFT calculator.
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

# Run vibrational analysis
vib = Vibrations(n2)
vib.run()

# Get frequencies
freqs = vib.get_frequencies()

print("Vibrational frequencies (cm^-1):")
print(freqs)

# Cleanup temporary files
vib.clean()
