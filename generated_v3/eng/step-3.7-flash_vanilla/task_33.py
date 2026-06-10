from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.005)
vib = Vibrations(atoms)
vib.run()
real_freqs = vib.get_frequencies()[vib.get_frequencies() > 0]
print("Real vibrational frequencies (cm⁻¹):", real_freqs)
