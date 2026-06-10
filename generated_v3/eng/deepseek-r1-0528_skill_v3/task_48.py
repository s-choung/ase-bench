from ase.build import bulk
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
positions = atoms.get_positions()
p1 = positions[0].reshape(1, 3)
p2 = positions
cell = atoms.cell
d_matrix = get_distances(p1, p2, cell=cell, pbc=(True, True, True))[1][0]
d_array = np.linalg.norm(d_matrix, axis=1)
d_array_nonzero = d_array[np.nonzero(d_array)]

print(f'Minimum distance: {d_array_nonzero.min():.4f} Å')
print(f'Maximum distance: {d_array_nonzero.max():.4f} Å')
