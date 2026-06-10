from ase.cluster import Icosahedron

# Create Au Icosahedron nanoparticle with no shells
atoms = Icosahedron('Au', radius=5.0, noshells=3)

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Calculate and print the center of mass
center_of_mass = atoms.center_of_mass()
print(f"Center of mass: {center_of_mass}")
