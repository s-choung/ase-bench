from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("N2")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="n2_vib")
vib.run()
freqs = vib.get_frequencies()

print("Vibrational frequencies (cm^-1):")
for f in freqs:
    print(f)

vib.clean()
