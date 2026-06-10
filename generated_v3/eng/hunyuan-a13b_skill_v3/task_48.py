from ase import Atoms
from ase.build import bulk
from ase climbs import get_distances

# Create a 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True, size=(2, 2, 2))

# Set up neighbor list with periodic boundary conditions
neigh = atoms.get_neighborlist()  # No explicit mic=True needed in get_distances

# Calculate distances to atom 0
dist_at_0 = get_distances([0], neigh, cell=atoms.cell, pbc=True)

# Extract distances to other atoms
distances = dist_at_0[0][1:]

# Find minimum and maximum distances
min_dist = atoms.get_distance(0, 1)
max_dist = atoms.get_distance(0, 2)

# Print results
print(f"Minimum distance: {min_dist:.4f} Å")
print(f"Maximum distance: {max_dist:.4f} Å")
