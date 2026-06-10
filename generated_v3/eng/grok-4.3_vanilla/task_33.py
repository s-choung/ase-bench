from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
atoms = Atoms('CH4', [(0,0,0),(0.63,0.63,0.63),(-0.63,-0.63,0.63),(-0.63,0.63,-0.63),(0.63,-0.63,-0.63)])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freq = vib.get_frequencies()
print([f for f in freq if f > 0])
vib.clean()
