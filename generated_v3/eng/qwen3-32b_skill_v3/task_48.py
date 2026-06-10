from ase import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
indices = list(range(1, len(atoms)))
distances = get_distances(atoms, [0], indices, mic=True)
print(f"Minimum distance: {distances.min():.4f} Å")
print(f"Maximum distance: {distances.max():.4f} Å")
