from ase import units
from ase.build import molecule
from ase.calculators.hookean import Hookean
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
d0 = atoms.get_distance(0, 1)
calc = Hookean()
for i in range(1, 5):
    calc.add_spring(0, i, d0, 50.0)
atoms.calc = calc

opt = BFGS(atoms)
opt.run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
for f in freqs:
    if f > 0:
        print(f)
