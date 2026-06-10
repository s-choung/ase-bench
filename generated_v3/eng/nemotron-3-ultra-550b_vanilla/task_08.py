from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

# Relax geometry
from ase.optimize import BFGS
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib.summary()
