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
real_freqs = freqs[np.isclose(freqs.imag, 0.0)].real
real_freqs = real_freqs[real_freqs > 0.0]

print(real_freqs)

vib.clean()
