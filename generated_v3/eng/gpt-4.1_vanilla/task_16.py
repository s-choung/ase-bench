from ase.build import fcc111, surface, bcc110
from ase.build import bulk
from ase.visualize import view

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10)
print('Number of atoms:', len(slab))
print('Cell size (Angstrom):')
print(slab.cell.lengths())
