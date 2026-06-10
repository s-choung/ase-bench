from ase import Atoms
from ase.build import bulk
from ase.io import write

# Create Cu FCC bulk and form a 2x2x2 supercell
atoms = bulk('Cu', 'fcc')
atoms.set_repeat((2, 2, 2))

# Calculate distances from atom 0 to all other atoms with mic=True
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

# Determine minimum and maximum distances
min_dist = min(distances)
max_dist = max(distances)

# Print the results
print("Minimum distance:", min_dist, "Å")
print("Maximum distance:", max_dist, "Å")
