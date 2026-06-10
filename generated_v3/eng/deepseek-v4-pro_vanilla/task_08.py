from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
for f in freqs:
    print(f)
