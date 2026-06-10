from ase.cluster import Icosahedron
import numpy as np

icos = Icosahedron('Au', noshells=3)
print(len(icos))
print(icos.get_center_of_mass())
