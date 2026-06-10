from ase.cluster import icosahedron
atoms = icosahedron('Au', 3)
print(len(atoms))
print(atoms.get_center_of_mass())
