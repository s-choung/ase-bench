from ase.cluster import Icosahedron
atoms = Icosahedron('Au', noshells=3)
print(len(atoms), atoms.get_center_of_mass())
