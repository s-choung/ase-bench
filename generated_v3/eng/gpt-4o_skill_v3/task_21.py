from ase.cluster import Icosahedron
from ase.data import atomic_numbers

atoms = Icosahedron('Au', noshells=3)
n_atoms = len(atoms)
com = atoms.get_center_of_mass()

print("Number of atoms:", n_atoms)
print("Center of mass:", com)
