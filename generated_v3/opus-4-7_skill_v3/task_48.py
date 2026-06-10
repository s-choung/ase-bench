from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
pos = atoms.get_positions()
dists = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print(f"Min distance: {dists.min():.4f} Å")
print(f"Max distance: {dists.max():.4f} Å")
