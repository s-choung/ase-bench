from ase.cluster.icosahedron import Icosahedron
from ase import Atoms

# Create Au icosahedron with 3 shells
cluster = Icosahedron('Au', noshells=3)

# Number of atoms
n_atoms = len(cluster)
print(f"Number of atoms: {n_atoms}")

# Center of mass
com = cluster.get_center_of_mass()
print(f"Center of mass: {com}")
