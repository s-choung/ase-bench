from ase import Atoms
from ase.geometry import get_distances

# CO2 molecule structure
positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]
symbols = ["C", "O", "O"]
CO2 = Atoms(symbols=symbols, positions=positions, cell=(10, 10, 10), pbc=False)

# Calculate interatomic distances
distances = get_distances(CO2)
print(distances)
