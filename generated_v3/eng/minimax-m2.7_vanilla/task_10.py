from ase.cluster import Octahedron

# Create a Cu octahedral nanoparticle with length=5
cluster = Octahedron('Cu', length=5)

# Print the number of atoms and the shape of the positions array
print('Number of atoms:', len(cluster))
print('Positions shape:', cluster.positions.shape)
