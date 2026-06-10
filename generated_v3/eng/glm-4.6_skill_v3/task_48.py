from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
dists = get_distances(atoms, 0, range(1, len(atoms)), mic=True)

print(f"Min: {dists.min():.3f} Å")
print(f"Max: {dists.max():.3f} Å")
