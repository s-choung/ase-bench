from ase.cluster.octahedron import Octahedron

atoms = Octahedron('Cu', length=5)

print(len(atoms))
print(atoms.positions.shape)
