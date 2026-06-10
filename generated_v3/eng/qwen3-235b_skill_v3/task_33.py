from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = molecule('CH4')

# Set calculator
atoms.calc = EMT()

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Perform vibrational analysis
vib = Vibrations(atoms, name='ch4_vib')
vib.run()

# Get frequencies (in cm^-1)
freqs = vib.get_frequencies()

# Print only real frequencies
real_freqs = freqs[freqs > 0]
print(real_freqs)

# Clean up vibration files
vib.clean()
