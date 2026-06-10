from ase.cluster.icosahedron import Icosahedron
from ase import Atoms

# Create an Au icosahedron nanoparticle with 3 shells
nanoparticle = Icosahedron('Au', noshells=3)

# Print number of atoms and center of mass
print(len(nanoparticle))
print(nanoparticle.get_center_of_mass())
