from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('CO2',
            positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
            cell=[10, 10, 10],
            pbc=False)

distances = get_distances(co2.positions, cell=co2.cell, pbc=co2.pbc)
print("Interatomic distances (Å):")
print(distances)
