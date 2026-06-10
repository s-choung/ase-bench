from ase import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
print(np.abs(freqs))
vib.clean()
