from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create CH4 molecule
ch4 = Atoms('CH4', positions=[
    [0, 0, 0],      # C
    [1, 1, 1],      # H
    [-1, 1, 1],     # H
    [1, -1, 1],     # H
    [1, 1, -1]      # H
])

# Attach calculator
ch4.calc = EMT()

# Optimize structure
dyn = BFGS(ch4)
dyn.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(ch4, name='ch4_vib')
vib.run()

# Get frequencies in cm⁻¹
frequencies = vib.get_frequencies()

# Filter and print real frequencies
real_freqs = frequencies[frequencies > 1e-3]  # Filter out imaginary/near-zero modes
print("Real vibrational frequencies (cm⁻¹):", np.round(real_freqs, 2))

# Clean up vibration files
vib.clean()
