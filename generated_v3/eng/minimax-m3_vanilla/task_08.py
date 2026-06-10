from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('N2', positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 1.10)])
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()
vib.summary()
print('\nVibrational frequencies (cm^-1):')
print(vib.get_frequencies())
vib.clean()
