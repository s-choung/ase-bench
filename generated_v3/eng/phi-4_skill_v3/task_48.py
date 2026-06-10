from ase.build import bulk
from ase.geometry import get_distances

# Create Cu FCC bulk and make a 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Calculate distances from atom 0 to all other atoms
distances, pairs = get_distances([0], list(range(1, len(atoms))), atoms.cell, pbc=True)

# Flatten the distances array to a 1D array
distances = distances.flatten()

# Print minimum and maximum distances
print("Minimum distance:", distances.min())
print("Maximum distance:", distances.max())
