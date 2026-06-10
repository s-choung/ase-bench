from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule
co2 = Atoms('CO2', positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)])

# Set cell to 10x10x10 box
co2.set_cell((10, 10, 10))
co2.set_pbc(False)

# Calculate interatomic distances
distances = get_distances(co2.get_positions(), indices=[0,1,2])[1][0]

print(distances)
