from ase.build import bulk
import numpy as np

# FCC Cu bulk, 2×2×2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)

# distances from atom 0 to all others (mic=True for PBC)
dists = atoms.get_distances(0, list(range(1, len(atoms))), mic=True)[0]

print(f"min distance = {dists.min():.3f} Å")
print(f"max distance = {dists.max():.3f} Å")
