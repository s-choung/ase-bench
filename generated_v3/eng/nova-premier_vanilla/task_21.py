from ase import Atoms
from ase.cluster.icosahedron import Icosahedron

cluster = Icosahedron('Au', noshells=3, latticeconstant=4.08)
print(f'Number of atoms: {len(cluster)}')
print(f'Center of mass: {cluster.get_center_of_mass()}')
