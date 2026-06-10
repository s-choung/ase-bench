from ase import Atoms
import numpy as np

positions = np.array([
    [0.0, 0.0, 0.0],
    [1.16, 0.0, 0.0],
    [-1.16, 0.0, 0.0],
])

atoms = Atoms(
    symbols=['C', 'O', 'O'],
    positions=positions,
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

dists = atoms.get_distances(0, [1, 2])
print(dists)
