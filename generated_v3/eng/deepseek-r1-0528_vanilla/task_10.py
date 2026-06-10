from ase.cluster import Octahedron

atoms = Octahedron('Cu', 5, latticeconstant=3.59)
print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.positions.shape}")
