from ase.build import nanotube

nanotube = nanotube(6, 6, length=4)
print('Number of atoms:', len(nanotube.get_positions()))
print('Cell info:', nanotube.get_cell())
