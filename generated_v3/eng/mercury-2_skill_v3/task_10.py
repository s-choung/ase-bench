from ase.cluster import Octahedron

atoms = Octahedron('Cu', length=5)

print(atoms.get_number_of_atoms())          # number of atoms
print(atoms.get_positions().shape)          # (N, 3) array shape
