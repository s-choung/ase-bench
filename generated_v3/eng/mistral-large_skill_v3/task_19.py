from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]], cell=[10, 10, 10], pbc=False)
distances = get_distances(co2.positions)[1]
print("C-O distances:", distances[0, 1], distances[0, 2])
print("O-O distance:", distances[1, 2])
