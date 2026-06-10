from ase.build import nanotube

cnt = nanotube(6, 6, length=4, symbol='C')
print(f'Number of atoms: {len(cnt)}')
print('Cell vectors:')
print(cnt.get_cell())
print('Cell lengths and angles:')
print(cnt.get_cell_lengths_and_angles())
