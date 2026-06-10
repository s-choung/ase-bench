from ase import Atoms
import numpy as np

# CO2: C at (0,0,0), O at ±1.16 Å along x
atoms = Atoms(
    symbols='COO',
    positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)],
    cell=[10, 10, 10],
    pbc=False,
)

# distances from C (index 0) to each O (indices 1,2)
dists, _ = atoms.get_distances(0, [1, 2])
print("C–O distances (Å):", dists)
