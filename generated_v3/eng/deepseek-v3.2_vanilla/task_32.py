from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

h2o = Atoms('H2O', positions=[(0, 0, 0), (0.757, 0.586, 0), (-0.757, 0.586, 0)])
h2o.calc = EMT()

opt = BFGS(h2o)
opt.run(fmax=0.01)

vib = Vibrations(h2o)
vib.run()
vib.summary()

modes = vib.get_frequencies()
for i, freq in enumerate(modes[:3]):
    if freq > 0:
        energy = freq * 0.000123984  # cm^-1 to eV conversion
        print(f'Mode {i+1}: {freq:.2f} cm^-1, {energy:.6f} eV')

vib.clean()
