from ase import Atoms
import numpy as np

atoms = Atoms(
    symbols=['O', 'C', 'O'],
    positions=[[-1.16, 0.0, 0.0], [0.0, 0.0, 0.0], [1.16, 0.0, 0.0]],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

d_c_o = atoms.get_distances(1, [0, 2], mic=False)
d_o_o = atoms.get_distances(0, [2], mic=False)

print("C-O distances (Å):", d_c_o)
print("O-O distance (Å):", d_o_o[0])
