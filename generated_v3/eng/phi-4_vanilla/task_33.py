from ase import Atoms
from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Define CH4 molecule
ch4 = molecule('CH4')

# Optimize structure using EMT calculator
ch4.set_cell([10, 10, 10, 90, 90, 90])
ch4.set_pbc([True, True, True])

calculator = 'emt'
opt = BFGS(ch4)
opt.run(fmax=0.5)

# Perform vibration calculation using EMT calculator
vib = Vibrations(ch4)
ch4.set_calculator(calculator)

vib.run([], fmin=0.001, fmax=0.05)

# Get real frequencies
frequencies = vib.get_frequencies()
real_frequencies = [freq for freq in frequencies if freq.imag < 1e-6]

# Print real frequencies
print("Real frequencies:", real_frequencies)
