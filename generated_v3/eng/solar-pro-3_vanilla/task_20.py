from ase import Atoms
from ase.build import nanotube

# (6,6) carbon nanotube, length = 4 atoms along the tube axis
C66 = nanotube('C', n=6, m=6, length=4)

# print number of atoms
print('Number of atoms:', len(C66))

# print cell information (shape, volume, dimensions)
print('Cell shape :', C66.cell.shape)
print('Cell volume:', C66.cell.volume)
print('Cell (Å):', C66.cell)
