from ase.atoms import Molecule
from ase.build import molecule
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT
import numpy as np

# Create an N2 molecule
n2 = Molecule('N2', positions=[(0, 0, 0), (0, 0, 1.1)])  # 1.1 Å is a rough guess for bond length

# Attach the EMT calculator
n2.set_calculator(EMT())

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib_results = vib.get_frequencies(units='cm^-1', epsilon=1e-4)

# Print the vibrational frequencies
print("Vibrational frequencies (cm^-1):", vib_results)

# Clean up
vib.clean()
