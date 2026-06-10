from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

# Build Cu FCC bulk 2x2x2 supercell
structure = bulk('Cu', 'fcc', a=3.61, size=(2, 2, 2))

# Calculate distances using get_distances and account for periodic boundary conditions
distances, indices = get_distances(structure, structure.positions[0])  # Distances from atom 0 to all other atoms
distances[0, 0] = np.inf  # Ignore self-distance of the site atom itself

# Mask distances with the pandas mask option to consider periodic boundary conditions
# Line 0,0 in the distance matrix would set the self-distance to infinity to ignore the zero distance row.

# Extract minimum and maximum distances from the flattened array of distances
min_distance = np.min(distances)
max_distance = np.max(distances)

# Print the minimum and maximum distances
print(f'Supercell Cu FCC minimum distance to atom 0: {min_distance:.3f}')
print(f'Supercell Cu FCC maximum distance to atom 0: {max_distance:.3f}')
