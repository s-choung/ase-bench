from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

mol = Atoms('N2', [(0, 0, 0), (0, 0, 1.1)])
mol.calc = EMT()
BFGS(mol).run(fmax=0.01)

vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()
print("Vibrational frequencies (cm^-1):", list(freqs.real))
vib.clean()
