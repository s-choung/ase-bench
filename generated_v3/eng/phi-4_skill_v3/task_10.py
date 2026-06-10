from ase.cluster import Octahedron

# Create the copper octahedron nanoparticle with a specified length
atoms = Octahedron('Cu', length=5)

# Print the number of atoms in the octahedron
print("Number of atoms:", len(atoms))

# Print the shape of the positions array
print("Shape of positions array:", atoms.positions.shape)
