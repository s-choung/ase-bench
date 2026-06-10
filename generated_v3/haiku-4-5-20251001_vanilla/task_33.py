from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

ch4 = molecule('CH4')
ch4.calc = EMT()

dyn = BFGS(ch4, trajectory='ch4_opt.traj')
dyn.run(fmax=0.01)

vib = Vibrations(ch4, name='ch4_vib')
vib.run()

frequencies = vib.get_frequencies()
real_frequencies = frequencies[frequencies > 0]

print("Real vibrational frequencies (cm^-1):")
for i, freq in enumerate(real_frequencies):
    print(f"Mode {i+1}: {freq:.2f}")
