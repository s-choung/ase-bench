from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
indices1, indices2 = [0], list(range(1, len(atoms)))
distances = atoms.get_distances(indices1, indices2, mic=True)
print(f"Minimum distance: {min(distances):.2f} Å")
print(f"Maximum distance: {max(distances):.2f} Å")
