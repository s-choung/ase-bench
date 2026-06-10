import numpy as np
from ase import Atoms

a = 5.43
symbols = ['Si', 'Si']
positions = np.array([[0, 0, 0], [a/4, a/4, a/4]])
cell = np.diag([a, a, a])
atoms = Atoms(symbols, positions=positions, cell=cell, pbc=True)
supercell = atoms.make_supercell([[3, 0, 0], [0, 3, 0], [0, 0, 3]])
print(len(supercell))
print(f"{supercell.get_volume():.2f} angstrom^3")
