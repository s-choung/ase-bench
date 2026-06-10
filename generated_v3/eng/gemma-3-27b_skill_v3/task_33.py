from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = Atoms('CH4', positions=[(0, 0, 0), (0.66, 0.66, 0.66), (-0.66, -0.66, 0.66),
                                 (-0.66, 0.66, -0.66), (0.66, -0.66, -0.66)])
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, calculator=atoms.calc)
vib.run()
frequencies = vib.get_frequencies()
real_frequencies = frequencies[np.isreal(frequencies)]
print(real_frequencies)
