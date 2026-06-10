from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Perform the vibration calculation
vib = Vibrations(atoms, name='vib')
vib.run()
frequencies = vib.get_frequencies()

# Filter and print only the real frequencies
real_frequencies = frequencies[frequencies.imag == 0].real
print("Real Frequencies (cm⁻¹):", real_frequencies)
