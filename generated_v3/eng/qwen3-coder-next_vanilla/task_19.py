from ase import Atoms
from ase.neighborlist import neighbor_list
import numpy as np

# Create CO2 molecule
atoms = Atoms('OCO', 
              positions=[(-1.16, 0.0, 0.0), (0.0, 0.0, 0.0), (1.16, 0.0, 0.0)])
atoms.set_cell([10, 10, 10])
atoms.pbc = False

# Calculate distances
distances = atoms.get_distances(0, 2, mic=False)
print(f"O-C distance: {distances:.2f} Å")
