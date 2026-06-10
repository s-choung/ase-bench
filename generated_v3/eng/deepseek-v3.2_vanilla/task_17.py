from ase.build import bulk, surface
from ase.visualize import view

atoms = bulk('Cu', 'fcc', a=3.6)
slab = surface(atoms, (2,1,1), layers=3, vacuum=10.0)

print(f'Number of atoms: {len(slab)}')
print('Cell:', slab.get_cell())
