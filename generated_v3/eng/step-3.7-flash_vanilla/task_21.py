from ase.cluster import Icosahedron
au_ico = Icosahedron('Au', noshells=3)
print(len(au_ico))
print(au_ico.get_center_of_mass())
