from ase.cluster.icosahedron import Icosahedron
from ase import Atoms

# Create Au icosahedron nanoparticle with 3 shells
cluster = Icosahedron('Au', 3)

# Print number of atoms
print(f"Number of atoms: {len(cluster)}")

# Calculate and print center of mass
com = cluster.get_center_of_mass()
print(f"Center of mass: {com}")
