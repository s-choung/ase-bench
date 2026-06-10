from ase.cluster import Icosahedron

atoms = Icosahedron('Au', noshells=3)
print("Number of atoms:", len(atoms))
print("Center of mass:", atoms.get_center_of_mass())
