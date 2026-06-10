from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
d = 1.1
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
n2.calc = EMT()

# Optimize structure
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(n2, name='vib')
vib.run()
freqs = vib.get_frequencies()

# Print frequencies
print(freqs)

# Cleanup
vib.clean()
