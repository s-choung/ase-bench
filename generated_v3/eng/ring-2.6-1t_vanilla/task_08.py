from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

N2 = molecule('N2')
N2.set_calculator(EMT())

# relax to equilibrium geometry
opt = BFGS(N2)
opt.run(fmax=0.05)

# compute vibrational modes
vib = Vibrations(N2)
vib.run()

freqs = vib.get_frequencies()
print('Vibrational frequencies (eV):')
for f in freqs:
    print(f)
