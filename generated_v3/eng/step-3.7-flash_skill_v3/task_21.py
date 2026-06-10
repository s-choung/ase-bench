from ase.cluster import Icosahedron

au_np = Icosahedron('Au', noshells=3)
print(len(au_np))
print(au_np.get_center_of_mass())
