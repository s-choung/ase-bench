from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Perform vibration calculation
vib = Vibrations(atoms)
vib.run()

# Get vibrational frequencies and filter real frequencies
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f > 0]

print("Real Vibrational Frequencies (cm⁻¹):", real_freqs)

vib.clean()
