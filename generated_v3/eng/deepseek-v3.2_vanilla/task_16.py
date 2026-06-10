from ase.build import bcc110
from ase.visualize import view

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0, periodic=True)
print(f'Number of atoms: {len(slab)}')
print(f'Cell size (Å): {slab.cell.lengths()}')
