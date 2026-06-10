from ase.build import fcc100
from ase import Atoms

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12, a=3.6)

print('Number of atoms:', len(slab))
print('Cell matrix:\n', slab.get_cell())
print('Cell lengths and angles:', slab.get_cell_lengths_and_angles())
