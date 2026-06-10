from ase.cluster import Icosahedron
from ase.io import write
import numpy as np

atoms = Icosahedron('Au', noshells=3)
print(len(atoms))
print(np.mean(atoms.positions, axis=0))
