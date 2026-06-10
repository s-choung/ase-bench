from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule
co2 = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]],
            cell=[10, 10, 10], pbc=False)

# Calculate interatomic distances
distances = get_distances(co2, mic=False)

# Print distances (upper triangular matrix, excl. diagonal)
for i in range(len(co2)):
    for j in range(i+1, len(co2)):
        print(f'Distance between atom {i} and {j}: {distances[i,j]:.2f} Å')
