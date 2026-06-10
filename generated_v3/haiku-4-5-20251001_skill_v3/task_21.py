from ase.cluster import Icosahedron
from ase.geometry import get_center_of_mass

atoms = Icosahedron('Au', noshells=3)
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass: {get_center_of_mass(atoms)}")
