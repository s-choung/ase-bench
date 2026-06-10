from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

mol = molecule('CH4')
mol.calc = EMT()

opt = BFGS(mol)
opt.run(fmax=0.01)

vib = Vibrations(mol)
vib.run()
vib.summary(method='standard')

real_freqs = [f for f in vib.get_frequencies() if f.imag == 0]
print("Real frequencies (cm^-1):", real_freqs)
