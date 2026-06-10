from ase.build import nanotube
from ase import units

tube = nanotube(6, 6, length=4)
print(f'Number of atoms: {len(tube)}')
print('Cell:', tube.get_cell())
