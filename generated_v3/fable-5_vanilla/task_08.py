from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib.summary()

for i, e in enumerate(vib.get_frequencies()):
    print(f"Mode {i}: {e.real:.2f} cm^-1")

vib.clean()
