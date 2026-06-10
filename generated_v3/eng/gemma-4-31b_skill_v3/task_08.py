from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule and set calculator
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize geometry before vibration analysis
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='vib_n2')
vib.run()
frequencies = vib.get_frequencies()

print(f"Vibrational frequencies (cm-1): {frequencies}")

# Cleanup vibration files
vib.clean()
