from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# Create a methane molecule
methane = molecule('CH4')

# Optimize the structure
calc = EMT()
methane.calc = calc
dyn = BFGS(methane, trajectory='methane_opt.traj')
dyn.run(fmax=0.02)

# Calculate vibrational frequencies
vib = Vibrations(methane)
vib.run()

# Filter and print real frequencies
frequencies = vib.frequencies
real_frequencies = frequencies[np.isreal(frequencies)]

for freq in real_frequencies:
    print(freq)
