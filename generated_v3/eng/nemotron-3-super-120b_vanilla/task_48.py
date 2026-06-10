from ase.build import bulk
import numpy as np

# Cu FCC bulk, 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms = cu * (2, 2, 2)

# distances from atom 0 to all atoms (mic=True for PBC)
dists = atoms.get_distances(0, np.arange(len(atoms)), mic=True)

# exclude self-distance (0)
other = dists[1:]

print("Minimum distance:", other.min())
print("Maximum distance:", other.max())
