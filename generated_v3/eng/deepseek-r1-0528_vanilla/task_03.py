from ase import Atoms
import numpy as np

a = 3.18
z0 = 1.58

v1 = [a, 0, 0]
v2 = [a * 0.5, a * np.sqrt(3) * 0.5, 0]

pos_mo = [0, 0, 0]
pos_s1 = [a / 3, a * np.sqrt(3) / 3, z0]
pos_s2 = [2 * a / 3, 2 * a * np.sqrt(3) / 3, -z0]

cell = [v1, v2, [0, 0, 1]]

atoms = Atoms('MoS2', positions=[pos_mo, pos_s1, pos_s2], cell=cell, pbc=[1,1,1])
atoms.center(vacuum=10, axis=2)
print(atoms.cell.cellpar())
