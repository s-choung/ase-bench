from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()
BFGS(n2).run(fmax=0.01)

vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()
print(freqs)
vib.summary()
vib.clean()
