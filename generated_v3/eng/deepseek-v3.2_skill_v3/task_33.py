from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

ch4 = Atoms('CH4', positions=[
    [0.0000, 0.0000, 0.0000],
    [0.6263, 0.6263, 0.6263],
    [-0.6263, -0.6263, 0.6263],
    [0.6263, -0.6263, -0.6263],
    [-0.6263, 0.6263, -0.6263]
])

ch4.calc = EMT()
opt = BFGS(ch4)
opt.run(fmax=0.01)

vib = Vibrations(ch4, name='ch4_vib')
vib.run()
freqs = vib.get_frequencies()

real_freqs = freqs[freqs > 0]
print('Real frequencies (cm⁻¹):')
for i, f in enumerate(real_freqs):
    print(f'{i+1:3d}: {f:8.2f}')

vib.summary()
vib.clean()
