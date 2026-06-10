from ase.build import bulk

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)

distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print("min distance:", distances.min())
print("max distance:", distances.max())
