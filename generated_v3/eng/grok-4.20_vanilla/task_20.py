from ase.build import nanotube

cnt = nanotube(6, 6, length=4)
print(len(cnt))
print(cnt.cell)
