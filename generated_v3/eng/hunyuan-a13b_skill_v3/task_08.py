from ase import Atoms
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = Atoms('N2', positions='0 0 0 0 0 1.08', cell='0 0 0 10 10 10', pbc=False)

# Set EMT calculator
n2.calc = EMT()

# Optimize the structure
from ase.optimize import BFGS
BFGS(n2).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2, name='vib')
vib.run()

# Print vibrational frequencies
print("Vibrational frequencies (cm⁻¹):", vib.get_frequencies())
