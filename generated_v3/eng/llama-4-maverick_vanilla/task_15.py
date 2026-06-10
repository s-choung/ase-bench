from ase import Atoms
from ase.build import fcc100

slab = fcc100('Cu', size=(3,3,3), vacuum=12)
print(f'Number of atoms: {len(slab)}')
print('Cell info:')
print(slab.cell)
