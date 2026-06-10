from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('CO2', positions=[[0.0, 0.0, 0.0],
                              [1.16, 0.0, 0.0],
                              [-1.16, 0.0, 0.0]],
            cell=[10.0, 10.0, 10.0], pbc=False)

d, _ = get_distances(co2.positions, co2.positions, cell=co2.cell, pbc=co2.pbc)
print(d)
