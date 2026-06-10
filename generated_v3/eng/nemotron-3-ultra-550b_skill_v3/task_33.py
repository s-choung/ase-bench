from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms, trajectory='ch4_opt.traj')
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_vib')
vib.run()
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]
print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f:.2f}")
vib.clean()
