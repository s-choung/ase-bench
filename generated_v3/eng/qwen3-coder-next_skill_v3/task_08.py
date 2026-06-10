from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
atoms = Atoms('N2', positions=[[0, 0, 0], [1.10, 0, 0]])
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
frequencies = vib.get_frequencies()

# Print vibrational frequencies (in cm^-1)
print('Vibrational frequencies (cm^-1):', frequencies)
vib.clean()
