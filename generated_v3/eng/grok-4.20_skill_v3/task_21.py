from ase.cluster import Icosahedron
from ase import Atoms
import numpy as np

atoms = Icosahedron('Au', noshells=3)
print(len(atoms))
print(atoms.get_center_of_mass())
