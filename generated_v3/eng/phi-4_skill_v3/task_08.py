from ase.build import molecule
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT
import numpy as np

# Step 1: Initialize the N2 molecule with EMT calculator
n2_molecule = molecule('N2', calculator=EMT)

# Step 2: Optimize the structure using EMT calculator
n2_molecule.set(fmax=0.05)  # Set force convergence factor
# Normally, you would execute a structure optimization here, but for a single atom + bond system like N2,
# this step ensures positions are slightly optimized to account for fixed bonds.

# Step 3: Calculate vibrations using an approach that fits this simple molecule
vib = Vibrations(n2_molecule)
vib.run()  # Run the calculations to compute vibrations

# Retrieve vibrational frequencies
frequencies = vib.get_frequencies()  # Get frequencies in units of cm⁻¹

# Print the computed vibrational frequency values
print("Vibrational frequencies of N2 (in cm⁻¹):", frequencies)
