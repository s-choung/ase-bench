from ase.cluster import Icosahedron

particle = Icosahedron('Au', noshells=3)
print(f"Number of atoms: {len(particle)}")
print(f"Center of mass: {particle.get_center_of_mass()}")
