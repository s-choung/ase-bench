from ase.build import bulk
atoms = bulk('Cu', 'fcc') * (2, 2, 2)
d = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(d.min(), d.max())
