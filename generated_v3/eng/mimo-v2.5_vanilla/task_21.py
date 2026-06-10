from ase.cluster import Icosahedron
from ase.data import atomic_numbers, chemical_symbols

# Create Au icosahedron with 3 shells
cluster = Icosahedron('Au', noshells=3, latticeconstant=4.08)

# Print results
print(f"Number of atoms: {len(cluster)}")
print(f"Center of mass: {cluster.get_center_of_mass()}")
