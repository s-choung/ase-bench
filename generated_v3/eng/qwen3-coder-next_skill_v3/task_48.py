from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

# Create Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (2, 2, 2)

# Calculate distances from atom 0 to all other atoms with mic=True
distances = get_distances([0], np.arange(len(atoms)), mic=True)[0]

# Print minimum and maximum distances (excluding 0 distance to itself)
min_dist = np.min(distances[1:])  # Skip the first distance (0.0)
max_dist = np.max(distances[1:])

print(f"Minimum distance: {min_dist:.4f} Å")
print(f"Maximum distance: {max_dist:.4f} Å")
