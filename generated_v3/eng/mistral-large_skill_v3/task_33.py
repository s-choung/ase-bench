from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and optimize CH4
atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibration calculation
vib = Vibrations(atoms, name='ch4_vib')
vib.run()
freqs = vib.get_frequencies()

# Filter and print real frequencies
real_freqs = freqs[freqs > 0]
print("Real vibrational frequencies (cm⁻¹):")
print(real_freqs)

vib.clean()
