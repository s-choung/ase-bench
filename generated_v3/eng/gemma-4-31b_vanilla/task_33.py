from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup molecule and calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Geometry optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Filter and print real frequencies
real_freqs = [f for f in frequencies if f > 0]
print("Real Vibrational Frequencies (eV):", real_freqs)
