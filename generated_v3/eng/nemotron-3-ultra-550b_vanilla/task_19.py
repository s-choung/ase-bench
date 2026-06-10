from ase import Atoms
import numpy as np

# Create CO2 molecule
positions = np.array([
    [0.0, 0.0, 0.0],      # C
    [-1.16, 0.0, 0.0],    # O
    [1.16, 0.0, 0.0]      # O
])
co2 = Atoms('CO2', positions=positions, cell=(10, 10, 10), pbc=False)

# Calculate and print all interatomic distances
distances = co2.get_distances(0, range(len(co2)), mic=False)
print(f"Distances from C (index 0): {distances}")

distances = co2.get_distances(1, range(len(co2)), mic=False)
print(f"Distances from O (index 1): {distances}")

distances = co2.get_distances(2, range(len(co2)), mic=False)
print(f"Distances from O (index 2): {distances}")

# Alternatively, full distance matrix
print("\nFull distance matrix:")
print(co2.get_all_distances(mic=False))
