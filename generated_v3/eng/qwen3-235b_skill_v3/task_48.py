from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
dists = get_distances(atoms.positions[0:1], atoms.positions, cell=atoms.cell, pbc=atoms.pbc)[1]
print(np.min(dists), np.max(dists))
