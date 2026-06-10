from ase.cluster import Octahedron

atoms = Octahedron('Cu', length=5)
print(len(atoms))
print(atoms.positions.shape)
