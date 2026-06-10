from ase.build import nanotube

cnt = nanotube(6, 6, length=4, periodic=True)
print(len(cnt))
print(cnt.get_cell())
