from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Set up N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])  # N2 bond length ~1.1 Å

# Set EMT calculator
n2.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib.summary()
