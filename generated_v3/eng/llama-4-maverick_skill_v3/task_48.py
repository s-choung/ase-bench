from ase import Atoms
from ase.build import bulk
import numpy as np

# Create a 2x2x2 Cu FCC supercell
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = cu_bulk.repeat((2, 2, 2))

# Calculate distances between atom 0 and all other atoms with MIC
distances = supercell.get_distances(0, range(len(supercell)), mic=True)

# Print minimum and maximum distances (excluding distance to itself)
print(np.min(distances[1:]), np.max(distances[1:]))
