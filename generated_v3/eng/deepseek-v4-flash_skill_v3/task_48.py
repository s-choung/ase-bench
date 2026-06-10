from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
pos = atoms.get_positions()
p0 = pos[0]
distances, _ = get_distances(p0, pos, cell=atoms.cell, pbc=atoms.pbc, mic=True)
d_others = distances[1:]  # exclude self-distance
print(f"Minimum distance: {d_others.min():.3f} Å")
print(f"Maximum distance: {d_others.max():.3f} Å")
