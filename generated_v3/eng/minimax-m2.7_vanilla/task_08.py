from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()

dyn = BFGS(atoms, logfile=None)
dyn.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

print("Vibrational frequencies (cm^-1):")
for freq in vib.get_frequencies():
    print(freq * 8065.54)
