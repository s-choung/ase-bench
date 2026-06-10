from ase import Atoms
import numpy as np

atoms = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[
        (0.0, 0.0, 0.0),
        (0.0, 1.16, 0.0),
        (0.0, -1.16, 0.0)
    ],
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

distances = atoms.get_distances()
print(distances)
