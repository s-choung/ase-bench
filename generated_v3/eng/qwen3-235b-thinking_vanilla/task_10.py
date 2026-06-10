from ase.cluster import Octahedron
atoms = Octahedron('Cu', 5)
print(len(atoms))
print(atoms.positions.shape)
