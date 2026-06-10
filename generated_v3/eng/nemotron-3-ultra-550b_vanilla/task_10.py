from ase.cluster import Octahedron

nanoparticle = Octahedron('Cu', length=5)
print(f"Number of atoms: {len(nanoparticle)}")
print(f"Positions shape: {nanoparticle.get_positions().shape}")
