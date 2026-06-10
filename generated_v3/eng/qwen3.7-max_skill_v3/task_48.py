from ase.build import bulk

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
dists = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"Minimum distance: {dists.min():.4f} Å")
print(f"Maximum distance: {dists.max():.4f} Å")
