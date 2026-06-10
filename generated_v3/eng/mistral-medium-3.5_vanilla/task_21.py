from ase.cluster import Icosahedron
from ase.calculators.emt import EMT

cluster = Icosahedron('Au', noshells=3)
cluster.calc = EMT()
print(f"Atoms: {len(cluster)}")
print(f"COM: {cluster.get_center_of_mass()}")
