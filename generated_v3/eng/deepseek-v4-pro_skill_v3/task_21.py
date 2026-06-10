from ase.cluster import Icosahedron

# Create Au icosahedron with 3 shells
atoms = Icosahedron('Au', noshells=3)

# Print number of atoms and center of mass
print(f"Number of atoms: {len(atoms)}")
print(f"Center of mass (x, y, z): {atoms.get_center_of_mass()}")
