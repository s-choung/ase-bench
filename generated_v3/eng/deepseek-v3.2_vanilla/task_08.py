from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create N2 molecule
d = 1.1
atoms = Atoms('N2', positions=[(0., 0., 0.), (0., 0., d)])
atoms.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib.summary()

# Extract and print frequencies
frequencies = []
for i in range(len(atoms) * 3):
    freq = vib.get_frequencies()[i]
    if freq > 0:
        frequencies.append(freq)

print(f"Vibrational frequencies (cm⁻¹): {np.array(frequencies):.2f}")
