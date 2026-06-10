from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))

dists, _ = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=atoms.pbc, mic=True)
dists = np.linalg.norm(dists, axis=1)

print("min distance:", dists.min())
print("max distance:", dists.max())
