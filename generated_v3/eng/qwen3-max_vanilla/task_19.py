from ase import Atoms
from ase.build import molecule

co2 = Atoms('CO2', positions=[
    [0.0, 0.0, 0.0],      # C at origin
    [-1.16, 0.0, 0.0],    # O left
    [1.16, 0.0, 0.0]      # O right
], pbc=False, cell=[10, 10, 10])

distances = co2.get_all_distances()
print(distances)
