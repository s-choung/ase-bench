from ase.cluster import Icosahedron
from ase.visualize import view
from ase.io import write

# Create Au icosahedron nanoparticle with 3 shells
au_cluster = Icosahedron('Au', noshells=3, lattice_constant=4.0)

# Print number of atoms and center of mass
print(f"Number of atoms: {len(au_cluster)}")
print(f"Center of mass: {au_cluster.get_center_of_mass()}")
