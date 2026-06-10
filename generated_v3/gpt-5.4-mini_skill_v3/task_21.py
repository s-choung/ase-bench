from ase.cluster import Icosahedron
from ase.data import atomic_masses
import numpy as np

atoms = Icosahedron('Au', noshells=3)

m = atoms.get_masses()
com = np.sum(atoms.get_positions() * m[:, None], axis=0) / np.sum(m)

print(len(atoms))
print(com)
