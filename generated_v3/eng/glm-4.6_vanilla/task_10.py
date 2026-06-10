from ase.cluster import Octahedron

atoms = Octahedron('Cu', size=5, latticeconstant=3.61)

print(len(atoms))
print(atoms.positions.shape)
