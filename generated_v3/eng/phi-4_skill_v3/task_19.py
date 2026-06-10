from ase import Atoms
from ase.geometry import get_distances

# Define the CO2 molecule manually
co2 = Atoms('C', 'O', 'O', positions=[[0, 0, 0], [1.16, 0, 0], [2*1.16, 0, 0]])

# Set cell to a 10x10x10 box with periodic boundary conditions set to False
co2_cell = Atoms([pos[0], pos[1], pos[2]])  # Ensure the positions are preserved correctly
co2.set_cell([10, 10, 10], pbc=False)

# Get interatomic distances
distances = get_distances(co2.get_positions())
co2.get_positions()  # Print positions to make sure they're correct (optional step)

# Print the interatomic distances
print("Interatomic distances:")
for dist, idx_pair in zip(distances, [(0, 1), (0, 2), (1, 2)]):
    print(f"Distance {idx_pair}: {dist}")
