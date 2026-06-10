from ase import Atoms
from ase.calculators.emt import EMT
import numpy as np

# Create CO2 molecule
co2 = Atoms('CO2', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)])

# Set cell and boundary conditions
co2.set_cell([10, 10, 10])
co2.set_pbc(False)

# Calculate and print interatomic distances
distances = co2.get_all_distances()
print(distances)
