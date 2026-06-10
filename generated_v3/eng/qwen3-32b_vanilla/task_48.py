from ase.build import bulk

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
distances = atoms.get_distances(0, mic=True)
print(f"Minimum distance: {min(distances):.3f} A")
print(f"Maximum distance: {max(distances):.3f} A")
