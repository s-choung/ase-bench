import numpy as np
from ase import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2,2,2))
dist = get_distances(atoms, [0], range(len(atoms)), mic=True)
dist = dist[dist > 0]
print(f"Min: {np.min(dist)}, Max: {np.max(dist)}")
