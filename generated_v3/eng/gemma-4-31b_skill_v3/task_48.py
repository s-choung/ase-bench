from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
dists = get_distances(atoms[0], atoms, mic=True)

print(f"Minimum distance: {dists.min():.4f}")
print(f"Maximum distance: {dists.max():.4f}")
