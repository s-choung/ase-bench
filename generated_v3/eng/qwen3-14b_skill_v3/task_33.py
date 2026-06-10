from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

real_freqs = freqs[freqs > 0]
print(real_freqs)
