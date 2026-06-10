from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)

p1 = atoms.positions[0]
p2 = atoms.positions[1:]

_, d = get_distances(p1, p2, cell=atoms.cell, pbc=atoms.pbc, mic=True)

print(f"Minimum distance: {d.min():.6f} Å")
print(f"Maximum distance: {d.max():.6f} Å")
