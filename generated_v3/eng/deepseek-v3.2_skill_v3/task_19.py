from ase import Atoms
from ase.geometry import get_distances

positions = [[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]]
co2 = Atoms('CO2', positions=positions, cell=[10, 10, 10], pbc=False)

distances, _ = get_distances(co2.get_positions(), cell=co2.cell, pbc=co2.pbc)
print(distances)
