from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule("CH4")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="ch4_vib")
vib.run()
freqs = vib.get_frequencies()
vib.clean()

real_freqs = freqs[np.abs(freqs.imag) < 1e-8].real

for f in real_freqs:
    print(f"{f:.2f} cm^-1")
