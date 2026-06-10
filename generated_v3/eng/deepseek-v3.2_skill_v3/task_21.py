from ase.cluster import Icosahedron
from ase import Atoms

cluster = Icosahedron('Au', noshells=3)
print(len(cluster))
print(cluster.get_center_of_mass())
