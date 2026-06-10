from ase import Atoms
import numpy as np

# Create CO2 molecule
co2 = Atoms('CO2', positions=[[0, 0, 0], [0, 0, 1.16], [0, 0, -1.16]])

# Set cell and PBC
co2.set_cell([10, 10, 10])
co2.set_pbc(False)

# Calculate interatomic distances
distances = co2.get_distances(mic=False)

# Print distances (upper triangle, excluding self-distances)
for i in range(len(co2)):
    for j in range(i+1, len(co2)):
        print(f'Distance between atom {i} and {j}: {distances[i,j]:.4f} Angstrom')
