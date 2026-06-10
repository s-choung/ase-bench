from ase.cluster import Octahedron
atoms = Octahedron('Cu', length=5)
print(len(atoms), atoms.get_positions().shape)
