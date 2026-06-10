from ase.build import fcc100
from ase.visualize import view

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

print('Number of atoms:', len(slab))
print('Cell:\n', slab.cell)

# view(slab)
