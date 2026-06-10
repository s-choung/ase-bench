from ase.build import bcc110, add_vacuum
from ase import units

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0 * units.angstrom)
print('Number of atoms:', len(slab))
print('Cell:', slab.get_cell_lengths_and_angles())
