from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase import molecule
from ase.calculators.emt import EMT

atoms = molecule('CH4')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.05)

vib = Vibrations(atoms)
vib.run()
vib.analyze()

for f in vib.frequencies:
    if f > 0:
        print(f)
