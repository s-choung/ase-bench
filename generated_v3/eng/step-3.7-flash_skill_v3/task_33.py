from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and optimize CH4 structure
atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Run vibration calculation
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

# Filter and print real (positive) frequencies
real_freqs = freqs[freqs > 0]
print("Real vibrational frequencies (cm⁻¹):")
print(real_freqs)
