from ase.build import bulk
from ase.ga.utilities import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
distances = get_distances(atoms, 0, range(1, len(atoms)), mic=True)
print(f"Min distance: {min(distances):.4f}, Max distance: {max(distances):.4f}")
