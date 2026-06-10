import numpy as np
from ase import Atoms

a = 3.16
vacuum = 10.0

positions = np.array([
    [0, 0, 0],  # Mo
    [1/3, 2/3, 0],  # S
    [2/3, 1/3, 0],  # S
])

cell = np.array([
    [a, 0, 0],
    [a/2, (a * np.sqrt(3))/2, 0],
    [0, 0, vacuum]
])

atoms = Atoms(symbols=['Mo', 'S', 'S'], positions=positions, cell=cell)
print("Cell size:\n", atoms.get_cell())
