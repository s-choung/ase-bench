from ase.build import nanotube
from ase.visualize import view

cnt = nanotube(6, 6, length=4)
print("Number of atoms:", len(cnt))
print("Cell info:", cnt.cell)
