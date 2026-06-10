from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Set up vibration calculation
vib = Vibrations(atoms)
vib.run()

# Get frequencies and filter real ones
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f > 0]

# Print real frequencies
print("Real vibrational frequencies (meV):")
for i, freq in enumerate(real_freqs):
    print(f"{i+1}: {freq:.2f}")
