from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))
distances = atoms.get_distances(0, range(len(atoms)), mic=True)
print(f"Min distance: {distances.min():.4f} Å")
print(f"Max distance: {distances.max():.4f} Å")
