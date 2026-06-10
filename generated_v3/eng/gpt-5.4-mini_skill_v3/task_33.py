from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='ch4_vib')
vib.run()
freqs = vib.get_frequencies()

real_freqs = [f for f in freqs if abs(f.imag) < 1e-8]
for f in real_freqs:
    print(f.real)

vib.clean()
