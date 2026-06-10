from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_vib')
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f.real for f in freqs if abs(f.imag) < 1e-8 and f.real > 0]

print(real_freqs)

vib.clean()
