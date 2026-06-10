from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

opt = BFGS(n2, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(n2, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()

for i, f in enumerate(freqs):
    print(f"mode {i}: {f}")

vib.clean()
