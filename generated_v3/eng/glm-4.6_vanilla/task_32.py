from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

h2o = Atoms('H2O', positions=[[0, 0, 0], [0.95, 0, 0], [0.24, 0.93, 0]])
h2o.calc = EMT()

vib = Vibrations(h2o)
vib.run()

freqs = vib.get_frequencies()
for i, freq in enumerate(freqs):
    if freq.imag == 0:
        freq_cm = freq * 33.35641  # THz to cm^-1
        energy_ev = freq * 0.00413567  # THz to eV
        print(f'Mode {i+1}: {freq_cm:.1f} cm^-1, {energy_ev:.4f} eV')

vib.clean()
