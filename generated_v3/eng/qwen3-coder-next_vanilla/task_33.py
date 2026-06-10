from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS
import numpy as np

# Create CH4 molecule
atoms = Atoms('CH4', positions=[
    [0.0, 0.0, 0.0],  # C
    [0.629, 0.629, 0.629],
    [-0.629, -0.629, 0.629],
    [-0.629, 0.629, -0.629],
    [0.629, -0.629, -0.629]
])
atoms.set_calculator(EMT())

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='ch4_vib')
vib.run()

# Get frequencies and filter real ones
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if np.isreal(f)]

# Print real frequencies (in cm^-1)
print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f:.2f}")
