from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

n2 = molecule('N2')
n2.set_calculator(EMT())
vib = Vibrations(n2)
vib.run()
freq = vib.get_frequencies()
print(np.round(freq[np.abs(freq) > 1e-2], 2))
