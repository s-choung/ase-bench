from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('CO2',
            positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)],
            cell=[10, 10, 10],
            pbc=False)

dist = get_distances(co2)

print('C–O distances:', dist[0, 1], dist[0, 2])
print('O–O distance:', dist[1, 2])
