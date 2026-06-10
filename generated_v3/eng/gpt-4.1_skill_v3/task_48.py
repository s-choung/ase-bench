from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
pos = atoms.get_positions()
cell = atoms.get_cell()
d, _ = get_distances(pos[0], pos, cell, mic=True)
dists = d[0]
print('min:', np.min(dists[dists>0]))
print('max:', np.max(dists))
