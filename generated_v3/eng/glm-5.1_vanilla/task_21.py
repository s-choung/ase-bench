from ase.cluster import Icosahedron

cluster = Icosahedron('Au', noshells=3)

print("Number of atoms:", len(cluster))
print("Center of mass:", cluster.get_center_of_mass())
