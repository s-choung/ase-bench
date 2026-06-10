from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
distances = get_distances([0], range(len(atoms)), atoms.get_positions(), atoms.get_cell(), pbc=True)[1][0]
print(f"Min distance: {distances.min():.3f} Å")
print(f"Max distance: {distances.max():.3f} Å")
