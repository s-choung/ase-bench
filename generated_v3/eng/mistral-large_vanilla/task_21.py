from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

cluster = Icosahedron('Au', noshells=3)
cluster.calc = EMT()
print(f"Number of atoms: {len(cluster)}")
print(f"Center of mass: {cluster.get_center_of_mass()}")
