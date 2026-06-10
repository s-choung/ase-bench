from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]
print(real_freqs)
