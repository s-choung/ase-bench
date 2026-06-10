from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f >= 0]
print("Real frequencies (cm^-1):", real_freqs)
