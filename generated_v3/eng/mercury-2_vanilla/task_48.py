from ase.build import bulk
import numpy as np

# Create a Cu FCC bulk and make a 2×2×2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Distances from atom 0 to all others, using minimum image convention
dists, _ = atoms.get_distances(0, list(range(1, len(atoms))), mic=True)

print("min distance:", np.min(dists))
print("max distance:", np.max(dists))
