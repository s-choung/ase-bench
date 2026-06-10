from ase import Atoms
from ase.build import bulk, surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu_bulk, (2,1,1), layers=3)
add_vacuum(slab, 10)

print(f'Number of atoms: {len(slab)}')
print('Cell:')
print(slab.get_cell())
