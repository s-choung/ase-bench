from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate the vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()

# Print the vibrational frequency values
print(freqs)
