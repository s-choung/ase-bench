from ase import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build CH4 and set EMT calculator
ch4 = molecule('CH4')
ch4.calc = EMT()

# Optimize structure
BFGS(ch4).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(ch4)
vib.run()

# Filter and print real frequencies (cm⁻¹)
real_freqs = [f for f in vib.get_frequencies().tocm() if f > 0]
print('Real frequencies (cm⁻¹):', real_freqs)
