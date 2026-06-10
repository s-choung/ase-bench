from ase.build import nanotube
from ase import units

# (6,6) carbon nanotube, length 4 Å
tube = nanotube(6, 6, length=4, symbol='C')

print('Number of atoms:', len(tube))
print('Cell matrix:\n', tube.get_cell())
print('Cell lengths and angles (a,b,c,alpha,beta,gamma):', tube.get_cell_lengths_and_angles())
