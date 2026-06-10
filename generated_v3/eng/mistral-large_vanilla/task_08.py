from ase import Atoms
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT

n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()
vib.summary()
freqs = vib.get_frequencies()
print("Vibrational frequencies (cm^-1):", freqs[6:])
