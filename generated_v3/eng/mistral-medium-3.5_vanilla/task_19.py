from ase import Atoms
from ase.calculators.emt import EMT

co2 = Atoms('CO2', positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)], cell=(10, 10, 10), pbc=False)
co2.calc = EMT()
distances = co2.get_distances()
print(distances)
