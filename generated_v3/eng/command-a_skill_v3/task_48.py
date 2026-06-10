from ase.build import bulk
from ase.geometry import get_distances

# Create a 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))

# Calculate distances from atom 0 to all other atoms
distances = get_distances(atoms, 0, mic=True)

# Print minimum and maximum distances
print(f"Minimum distance: {distances.min():.4f} Å")
print(f"Maximum distance: {distances.max():.4f} Å")
