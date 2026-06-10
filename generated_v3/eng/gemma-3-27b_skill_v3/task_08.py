from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()
dyn = Vibrations(atoms, name='N2_vibrations')
dyn.run()

frequencies = dyn.get_frequencies()
print(frequencies)
