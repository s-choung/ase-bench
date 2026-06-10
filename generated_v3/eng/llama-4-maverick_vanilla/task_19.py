from ase import Atoms
from ase.calculators.emt import EMT

co2 = Atoms('CO2', positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)])
co2.set_cell((10, 10, 10))
co2.set_pbc(False)
co2.set_calculator(EMT())

distances = co2.get_distances(1, [0, 2], mic=False)
print(distances)
