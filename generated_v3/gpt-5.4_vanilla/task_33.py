from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import os

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_vib')
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if abs(getattr(f, 'imag', 0.0)) < 1e-12 and float(getattr(f, 'real', f)) > 0.0]

for f in real_freqs:
    print(float(getattr(f, 'real', f)))

vib.clean()
for fn in ['ch4_vib.eq.pckl', 'ch4_vib.json']:
    if os.path.exists(fn):
        os.remove(fn)
