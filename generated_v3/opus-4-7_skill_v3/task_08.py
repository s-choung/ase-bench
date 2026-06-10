from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='vib_n2')
vib.run()
freqs = vib.get_frequencies()
print("Frequencies (cm^-1):", freqs)
vib.summary()
vib.clean()
