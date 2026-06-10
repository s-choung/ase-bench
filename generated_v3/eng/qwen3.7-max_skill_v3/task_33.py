from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f.real for f in freqs if f.imag == 0 and f.real > 10.0]

for f in real_freqs:
    print(f"{f:.2f} cm^-1")
