from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (2, 2, 2)
distances = get_distances(atoms, 0, mic=True)
min_distance = np.min(distances)
max_distance = np.max(distances)

print(f"Minimum distance: {min_distance}")
print(f"Maximum distance: {max_distance}")
