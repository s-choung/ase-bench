from ase import Atoms
from ase.geometry import get_distances
import numpy as np

atoms = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[(0.0, 0.0, 0.0), (1.16, 0.0, 0.0), (-1.16, 0.0, 0.0)],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

dists, _ = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc)
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f"{atoms[i].symbol}-{atoms[j].symbol}: {dists[i, j]:.3f} Å")
