from ase.build import fcc111, molecule
import numpy as np

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0, orthogonal=True)
top_z = max(slab.positions[:, 2])
pos8, pos9 = slab[8].position, slab[9].position
mid_x, mid_y = (pos8[0] + pos9[0]) / 2.0, (pos8[1] + pos9[1]) / 2.0
n2 = molecule('N2')
bond_length = np.linalg.norm(n2[1].position - n2[0].position)
al_vec = pos9 - pos8
al_vec[2] = 0
al_vec_unit = al_vec / np.linalg.norm(al_vec)
center = np.array([mid_x, mid_y, top_z + 2.0])
n2[0].position = center - al_vec_unit * (bond_length / 2)
n2[1].position = center + al_vec_unit * (bond_length / 2)
system = slab + n2
print(len(system))
print(set(atom.symbol for atom in system))
