from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

ch4 = molecule('CH4')
ch4.calc = EMT()
BFGS(ch4).run(fmax=0.01)

vib = Vibrations(ch4, name='ch4_vib')
vib.run()

freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if abs(f.imag) < 1e-5]

print("Real vibrational frequencies (cm^-1):")
for f in real_freqs:
    print(f"  {f.real:10.2f}")
