from ase.build import bulk
atoms = bulk('Cu', 'fcc') * (2, 2, 2)
dists = atoms.get_distances(0, range(len(atoms)), mic=True)[0]
other_dists = dists[1:]
print(min(other_dists), max(other_dists))
