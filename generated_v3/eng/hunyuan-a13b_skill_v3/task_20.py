from ase import Atoms
from ase.cluster import nanotube

n, m = 6, 6
length = 4
cnt = nanotube(n, m, length=length)
print("Number of atoms:", len(cnt))
print("Cell info:", cnt.cell)
