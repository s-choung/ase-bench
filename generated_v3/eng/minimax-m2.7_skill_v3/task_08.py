from ase.atoms import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
print("Vibrational frequencies (cm⁻¹):")
print(freqs)
vib.summary()
vib.clean()
