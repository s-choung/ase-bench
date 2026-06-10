from ase import Atoms
from ase.build import molecule
from ase.calculators import EMT
from ase.vibrations import Vibrations

# Define CH4 molecule
mol = molecule('C; H4$, mm=ccp4')

# Optimize structure with EMT
mol.calc = EMT()
Optimize = BFGS(mol)
Optimize.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(mol, name='vib')
vib.run()

# Extract real frequencies (cm-1)
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]  # Filter out imaginary frequencies

# Print real frequencies
print(real_freqs)
