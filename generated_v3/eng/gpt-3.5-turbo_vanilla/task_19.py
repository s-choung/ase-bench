from ase import Atoms
from ase.calculators.emt import EMT

CO2 = Atoms('CO2', positions=[[0.0, 0.0, 0.0], [1.16, 0.0, 0.0], [-1.16, 0.0, 0.0]],
            calculator=EMT())

CO2.set_cell([10, 10, 10], scale_atoms=False)
CO2.pbc = False

distances = CO2.get_distances(0, [1, 2])
print(distances)
