from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

cluster = Icosahedron('Au', noshells=3, latticeconstant=4.05)
cluster.calc = EMT()
print(len(cluster))
print(cluster.get_center_of_mass())
