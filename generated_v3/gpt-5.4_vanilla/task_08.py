from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

vib = Vibrations(atoms, name='n2_vib')
vib.run()

freqs = vib.get_frequencies()
for f in freqs:
    print(f)

vib.clean()
