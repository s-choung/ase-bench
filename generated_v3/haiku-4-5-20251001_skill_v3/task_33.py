from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_vib')
vib.run()

freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]

print("Real vibrational frequencies (cm⁻¹):")
for i, freq in enumerate(real_freqs):
    print(f"Mode {i+1}: {freq:.2f}")

vib.clean()
