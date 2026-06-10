from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True).repeat((2, 2, 2))
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(f"Min distance: {distances.min():.3f} Å")
print(f"Max distance: {distances.max():.3f} Å")
