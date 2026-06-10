from ase import Atoms
import numpy as np

a = 2.95
c = a * 1.59
atoms = Atoms('Ti',
              positions=[[0, 0, 0], [2/3, 1/3, 0.5]],
              cell=[[a, 0, 0],
                    [-a/2, a*np.sqrt(3)/2, 0],
                    [0, 0, c]],
              pbc=True)

print("Cell vectors:")
print(atoms.get_cell())
print("Atomic positions:")
print(atoms.get_positions())
