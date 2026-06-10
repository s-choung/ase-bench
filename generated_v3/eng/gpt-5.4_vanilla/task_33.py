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

energies = vib.get_energies()
freqs_cm1 = np.array([e.real for e in energies if abs(e.imag) < 1e-12]) / 0.0001239841984332003

print('Real vibrational frequencies (cm^-1):')
for f in freqs_cm1:
    if f > 1e-6:
        print(f'{f:.2f}')

vib.clean()
