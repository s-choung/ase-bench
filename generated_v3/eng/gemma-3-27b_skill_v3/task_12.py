from ase import Atoms
from ase.build import bulk
import numpy as np

a = 2.95
c_over_a = 1.59
c = a * c_over_a

cell = np.array([[a, 0, 0],
                 [-a/2, a*np.sqrt(3)/2, 0],
                 [0, 0, c]])

atoms = bulk('Ti', crystalstructure='hcp', cell=cell)

print("Cell Vectors:")
print(cell)
print("\nAtomic Positions:")
print(atoms.positions)
