from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)
pairs = [(0, i) for i in range(1, len(atoms))]
distances = get_distances(atoms, pairs, mic=True)
print(f"Minimum distance: {min(distances)} Å")
print(f"Maximum distance: {max(distances)} Å")
