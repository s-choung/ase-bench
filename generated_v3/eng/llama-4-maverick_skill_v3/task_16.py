from ase import Atoms
from ase.build import bcc110

slab = bcc110('Fe', size=(2,2,4), vacuum=10)
print(f'Number of atoms: {len(slab)}')
print(f'Cell size: {slab.get_cell()}')
