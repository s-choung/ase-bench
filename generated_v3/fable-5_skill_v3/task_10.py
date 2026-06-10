from ase.cluster import Octahedron

atoms = Octahedron('Cu', length=5)
print("Number of atoms:", len(atoms))
print("Positions shape:", atoms.get_positions().shape)
