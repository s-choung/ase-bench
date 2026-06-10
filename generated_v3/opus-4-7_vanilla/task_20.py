from ase.build import nanotube

cnt = nanotube(6, 6, length=4)
print("Number of atoms:", len(cnt))
print("Cell:")
print(cnt.cell)
