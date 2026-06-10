from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = [f.real for f in vib.get_frequencies() if abs(f.imag) < 1e-3 and f.real > 0]
print(freqs)
vib.clean()
