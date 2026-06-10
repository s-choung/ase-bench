from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

BFGS(n2).run(fmax=1e-4)

vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()
print("Vibrational frequencies (cm^-1):")
for i, f in enumerate(freqs):
    print(f"Mode {i}: {f}")
vib.summary()
