from ase import Atoms
from ase.geometry import get_distances
import numpy as np

atoms = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[(0.0, 0.0, 0.0), (-1.16, 0.0, 0.0), (1.16, 0.0, 0.0)],
    cell=[10.0, 10.0, 10.0],
    pbc=False
)

d, _ = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=atoms.pbc)
print("C-O distances:", d)

d_oo, _ = get_distances(atoms.positions[1], atoms.positions[2], cell=atoms.cell, pbc=atoms.pbc)
print("O-O distance:", d_oo)
