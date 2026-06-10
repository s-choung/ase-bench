from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

# Print frequencies in cm^-1
print('Vibrational frequencies (cm^-1):', freqs)
