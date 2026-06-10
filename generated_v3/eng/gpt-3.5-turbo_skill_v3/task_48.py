from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', crystalstructure='fcc', a=3.6, cubic=True) * (2, 2, 2)

distances = get_distances(0, range(len(atoms)), atoms.get_cell(), mic=True)
min_distance = distances[distances > 0].min()
max_distance = distances.max()

print(f"Minimum distance between atom 0 and others: {min_distance:.2f} Å")
print(f"Maximum distance between atom 0 and others: {max_distance:.2f} Å")
