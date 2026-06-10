from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build N2 molecule
n2 = molecule('N2')
# Set EMT calculator
n2.calc = EMT()
# Optimize structure
BFGS(n2).run(fmax=0.01)
# Calculate vibrations
vib = Vibrations(n2)
vib.run()
# Get and print frequencies (cm⁻¹)
freqs = vib.get_frequencies()
print(freqs)
vib.clean()
