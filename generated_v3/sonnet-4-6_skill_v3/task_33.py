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
vib.summary()

real_freqs = freqs[freqs.imag == 0].real
real_freqs = real_freqs[real_freqs > 0]

print("\n실수 진동수 (cm⁻¹):")
for i, f in enumerate(real_freqs):
    print(f"  Mode {i+1}: {f:.2f} cm⁻¹")

vib.clean()
