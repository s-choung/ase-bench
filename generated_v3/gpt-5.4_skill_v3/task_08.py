from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='n2_vib')
vib.run()

freqs = vib.get_frequencies()
print(freqs)

vib.clean()
