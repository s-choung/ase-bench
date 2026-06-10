from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

p1 = atoms.positions[0][None, :]
p2 = atoms.positions[1:]
D, _ = get_distances(p1, p2, cell=atoms.cell, pbc=atoms.pbc, mic=True)
distances = D[0]

print(f"min distance: {np.min(distances):.6f} Å")
print(f"max distance: {np.max(distances):.6f} Å")
