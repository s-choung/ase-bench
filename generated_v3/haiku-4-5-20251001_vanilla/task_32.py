from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

h2o = molecule('H2O')
h2o.calc = EMT()

vib = Vibrations(h2o, indices=[0, 1, 2])
vib.run()

vib.summary()

hc = 1.23984198e-4  # eV*cm
frequencies = vib.get_frequencies()

print("\n=== Vibrational Modes ===")
for i, freq in enumerate(frequencies):
    if freq > 0:
        wavenumber = freq / hc
        energy = freq
        print(f"Mode {i+1}: {wavenumber:.2f} cm^-1, {energy:.6f} eV")
    else:
        print(f"Mode {i+1}: Imaginary frequency (translation/rotation)")
