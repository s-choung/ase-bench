from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('CH4')
atoms.center(vacuum=5.0)
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
energies = vib.get_energies()

real_freqs = []
for e in energies:
    if np.isreal(e) and e.real > 0 and abs(e.imag) < 1e-8:
        real_freqs.append(e.real * 8065.544)

print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f:.2f}")

vib.clean()
