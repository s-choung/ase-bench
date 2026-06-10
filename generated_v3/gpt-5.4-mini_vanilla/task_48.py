from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)

d = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=atoms.pbc, mic=True)[1]
distances = np.linalg.norm(d, axis=1)

print("min distance:", distances.min())
print("max distance:", distances.max())
