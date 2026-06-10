from ase.build import octahedron

atoms = octahedron('Cu', a=3.6, length=5)
print(len(atoms))
print(atoms.positions.shape)
