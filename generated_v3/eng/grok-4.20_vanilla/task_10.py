from ase.cluster import Octahedron
import numpy as np

atoms = Octahedron('Cu', length=5, cutoff=0)
print(len(atoms))
print(np.array(atoms.get_positions()).shape)
