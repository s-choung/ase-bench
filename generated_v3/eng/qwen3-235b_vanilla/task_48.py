from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

# Create Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)

# Get positions
positions = cu.get_positions()

# Calculate distances from atom 0 to all others with MIC
distances = get_distances(positions, positions[0:1], cell=cu.get_cell(), pbc=True)[0]

# Remove self-distance (atom 0 to itself) for min calculation
nonzero_distances = distances[distances > 1e-6]

# Print min and max distances
print(f"Minimum distance: {np.min(nonzero_distances):.4f} Å")
print(f"Maximum distance: {np.max(distances):.4f} Å")
