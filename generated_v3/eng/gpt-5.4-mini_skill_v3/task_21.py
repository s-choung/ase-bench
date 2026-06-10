from ase.cluster import Icosahedron
from ase.data import atomic_masses
import numpy as np

atoms = Icosahedron('Au', noshells=3)

m = np.array([atomic_masses[a.number] for a in atoms])
com = (atoms.get_positions() * m[:, None]).sum(axis=0) / m.sum()

print(len(atoms))
print(com)
