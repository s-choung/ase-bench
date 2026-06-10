from ase.build import bulk
atoms = bulk('Cu', 'fcc').multiply(2)
dists = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(f"Min distance: {min(dists):.4f}, Max distance: {max(dists):.4f}")
