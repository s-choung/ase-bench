from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
methane = molecule('CH4')

# Set the EMT calculator
methane.calc = EMT()

# Optimize the structure using BFGS
optimizer = BFGS(methane)
optimizer.run(fmax=0.01)  # fmax is the RMS force threshold

# Perform the vibrational frequency calculation
vib = Vibrations(methane)
vib.run()

# Extract frequencies (in cm⁻¹)
frequencies = vib.get_frequencies()

# Filter and print real frequencies
real_frequencies = frequencies.real[frequencies.imag == 0]
print("Real vibrational frequencies (in cm⁻¹):", real_frequencies)

# Cleanup the vibrations data
vib.clean()
