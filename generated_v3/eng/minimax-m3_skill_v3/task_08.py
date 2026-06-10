from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib.summary()
print('\nFrequencies (cm^-1):', vib.get_frequencies())
vib.clean()
