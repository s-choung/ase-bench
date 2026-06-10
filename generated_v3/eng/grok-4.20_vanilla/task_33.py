from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create CH4 molecule
atoms = Atoms('CH4',
              positions=[[0, 0, 0],
                         [0.5, 0.5, 0.5],
                         [-0.5, 0.5, -0.5],
                         [0.5, -0.5, -0.5],
                         [-0.5, -0.5, 0.5]],
              cell=[10, 10, 10])
atoms.center(vacuum=5.0)
atoms.set_calculator(EMT())

# Optimize structure
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

# Compute vibrations
vib = Vibrations(atoms, name='ch4_vib', delta=0.01)
vib.run()

# Get frequencies in cm^-1
freqs = vib.get_frequencies()

# Filter and print only real frequencies (exclude imaginary)
real_freqs = [f for f in freqs if f > 0]
print('Real vibrational frequencies (cm^-1):')
for f in real_freqs:
    print(f'{f:.2f}')
