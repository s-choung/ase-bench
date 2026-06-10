from ase.cluster import octahedron

cluster = octahedron('Cu', length=5)
print('Number of atoms:', len(cluster))
print('Positions shape:', cluster.get_positions().shape)
