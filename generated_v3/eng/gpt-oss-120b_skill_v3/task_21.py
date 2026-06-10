from ase.cluster import Icosahedron

# Au icosahedral nanoparticle, 3 shells
nanoparticle = Icosahedron('Au', noshells=3)

print(len(nanoparticle))                 # number of atoms
print(nanoparticle.get_center_of_mass()) # center of mass (Å)
