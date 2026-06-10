from ase import Atoms
from ase.calculators.emt import EMT

co2 = Atoms('CO2', positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)])
co2.set_cell([10, 10, 10])
co2.set_pbc(False)

distances = co2.get_distances(0, [1, 2])
print("C-O distances:", distances)
distances = co2.get_distances(1, 2)
print("O-O distance:", distances[0])
