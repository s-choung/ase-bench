from ase.build import bulk

# Build Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Compute distances from atom 0 to all atoms with minimum image convention
distances = atoms.get_distances(0, range(len(atoms)), mic=True)

# Exclude self-distance (zero)
distances = distances[distances > 0]

print("Minimum distance:", distances.min())
print("Maximum distance:", distances.max())
