from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
pos = atoms.get_positions()
d, _ = get_distances(pos[0], pos[1:], cell=atoms.cell, pbc=True, mic=True)
d = d.flatten()
print(np.min(d), np.max(d))
