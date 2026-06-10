from ase.cluster import Icosahedron
atoms = Icosahedron('Au', length=3, noshells=3)
print(len(atoms))
print(atoms.get_positions().mean(axis=0))
