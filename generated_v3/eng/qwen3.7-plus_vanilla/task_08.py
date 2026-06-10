from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()

for freq in vib.get_frequencies():
    print(freq)
