from ase.cluster import Icosahedron
atoms = Icosahedron('Au', length=3)
print(len(atoms))
print(atoms.get_center_of_mass())
