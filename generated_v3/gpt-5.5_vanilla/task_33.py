from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule("CH4")
atoms.center(vacuum=5.0)
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="ch4_emt_vib")
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f.real for f in freqs if abs(f.imag) < 1e-6 and f.real > 1.0]

print(real_freqs)

vib.clean()
