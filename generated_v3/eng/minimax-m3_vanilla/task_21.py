from ase.cluster import Icosahedron
from ase.build import bulk

# Get Au lattice constant from FCC bulk
a = bulk('Au', 'fcc').get_cell()[0, 0]

# Create Au icosahedron nanoparticle with 3 shells
atoms = Icosahedron('Au', noshells=3, latticeconstant=a)

print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {atoms.get_center_of_mass()}")
