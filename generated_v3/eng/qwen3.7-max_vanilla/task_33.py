from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

ch4 = molecule('CH4', vacuum=5.0)
ch4.calc = EMT()

BFGS(ch4, logfile=None).run(fmax=0.01)

vib = Vibrations(ch4)
vib.run()

freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]

print("Real frequencies (cm^-1):")
for f in real_freqs:
    print(f"{f:.2f}")
