from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = molecule('N2')
n2.calc = EMT()
BFGS(n2).run(fmax=0.005)
vib = Vibrations(n2)
vib.run()
print("Vibrational frequencies (cm⁻¹):", vib.get_frequencies().round(2))
vib.clean()
