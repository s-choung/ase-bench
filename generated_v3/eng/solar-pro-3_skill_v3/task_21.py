from ase.cluster import Icosahedron

# Icosahedron with 3 shell layers (noshells=3)
atoms = Icosahedron('Au', length=6.0, noshells=3)

print('Number of atoms:', len(atoms))
print('Center of mass:', atoms.center_of_mass())
