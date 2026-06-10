import numpy as np
from ase import Atoms

a = 2.95
c = a * 1.59

cell = np.array([[a, 0, 0],
                 [a/2, (a * np.sqrt(3))/2, 0],
                 [0, 0, c]])

positions = np.array([[0.0, 0.0, 0.0],
                      [2*a/3, a*np.sqrt(3)/3, c/2]])

atoms = Atoms(symbols=['Ti', 'Ti'], positions=positions, cell=cell, pbc=True)

print("Cell vectors:")
for vec in atoms.get_cell():
    print(vec)
print("\nAtomic positions:")
for pos in atoms.get_positions():
    print(pos)
