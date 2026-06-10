from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

n2 = molecule('N2')
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()
print(vib.get_frequencies())
