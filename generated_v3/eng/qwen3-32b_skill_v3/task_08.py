from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = molecule('N2')
n2.calc = EMT()

# Optimize geometry
BFGS(n2).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()
print(frequencies)
