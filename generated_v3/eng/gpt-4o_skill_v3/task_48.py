from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
positions = atoms.get_positions()

distances, _ = get_distances(positions[0], positions, cell=atoms.get_cell(), pbc=True)

min_distance = np.min(distances[distances > 0])  # Exclude zero distance (distance to itself)
max_distance = np.max(distances)

print(f"Minimum distance: {min_distance:.2f} Å")
print(f"Maximum distance: {max_distance:.2f} Å")
