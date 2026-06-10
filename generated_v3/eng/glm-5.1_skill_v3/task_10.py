from ase.cluster import Octahedron

atoms = Octahedron('Cu', length=5)
print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.get_positions().shape}")
