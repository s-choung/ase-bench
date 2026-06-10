from tempfile import TemporaryDirectory
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("N2")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=1e-4)

with TemporaryDirectory() as tmp:
    vib = Vibrations(atoms, name=f"{tmp}/n2")
    vib.run()
    freqs = vib.get_frequencies()
    vib.clean()

for i, f in enumerate(freqs, 1):
    print(f"{i}: {f} cm^-1")
