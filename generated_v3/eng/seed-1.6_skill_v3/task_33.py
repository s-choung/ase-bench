from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build and optimize CH4
ch4 = molecule('CH4')
ch4.calc = EMT()
BFGS(ch4).run(fmax=0.01)

# Vibrational calculation
vib = Vibrations(ch4)
vib.run()
freqs = vib.get_frequencies()

# Filter and print real frequencies (exclude numerical noise)
real_freqs = [f for f in freqs if f > 1e-6]
print(real_freqs)

vib.clean()
