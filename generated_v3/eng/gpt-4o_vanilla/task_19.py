from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

# Create CO2 molecule
positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]
symbols = ['C', 'O', 'O']
co2 = Atoms(symbols, positions=positions, cell=(10, 10, 10), pbc=False)

# Assign calculator
co2.set_calculator(EMT())

# Calculate distances
distances = co2.get_distances(0, [1, 2], mic=False)

# Print distances
print('CO distances: CO1 =', distances[0], 'angstroms, CO2 =', distances[1], 'angstroms')
