from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Define N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])

# Assign EMT calculator
n2.calc = EMT()

# Set up and run vibrational analysis
vib = Vibrations(n2)
vib.run()

# Get and print vibrational frequencies
frequencies = vib.get_frequencies()
print('Vibrational frequencies (cm^-1):', frequencies)

# Clean up temporary files
vib.clean()
