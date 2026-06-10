from ase.build import bulk

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"Minimum distance: {distances.min():.4f} Å")
print(f"Maximum distance: {distances.max():.4f} Å")
